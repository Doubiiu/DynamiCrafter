import os
import time
from omegaconf import OmegaConf
import torch
from scripts.evaluation.funcs import load_model_checkpoint, save_videos, batch_ddim_sampling, get_latent_z
from utils.utils import instantiate_from_config
from huggingface_hub import hf_hub_download
from einops import repeat
import torchvision.transforms as transforms
from pytorch_lightning import seed_everything


class Image2Video():
    def __init__(self,result_dir='./tmp/',gpu_num=1) -> None:
        self.download_model()
        self.result_dir = result_dir
        if not os.path.exists(self.result_dir):
            os.mkdir(self.result_dir)
        ckpt_path='checkpoints/dynamicrafter_256_v1/model.ckpt'
        config_file='configs/inference_256_v1.0.yaml'
        config = OmegaConf.load(config_file)
        model_config = config.pop("model", OmegaConf.create())
        model_config['params']['unet_config']['params']['use_checkpoint']=False   
        model_list = []
        for gpu_id in range(gpu_num):
            model = instantiate_from_config(model_config)
            # model = model.cuda(gpu_id)
            assert os.path.exists(ckpt_path), "Error: checkpoint Not Found!"
            model = load_model_checkpoint(model, ckpt_path)
            model.eval()
            model_list.append(model)
        self.model_list = model_list
        self.save_fps = 8

    def get_image(self, image, prompt, steps=50, cfg_scale=7.5, eta=1.0, fs=3, seed=123):
        seed_everything(seed)
        transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(256),
            ])
        torch.cuda.empty_cache()
        print('start:', prompt, time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        start = time.time()
        gpu_id=0
        if steps > 60:
            steps = 60 
        model = self.model_list[gpu_id]
        model = model.cuda()
        batch_size=1
        channels = model.model.diffusion_model.out_channels
        frames = model.temporal_length
        h, w = 256 // 8, 256 // 8
        noise_shape = [batch_size, channels, frames, h, w]

        # text cond
        text_emb = model.get_learned_conditioning([prompt])

        # img cond
        img_tensor = torch.from_numpy(image).permute(2, 0, 1).float().to(model.device)
        img_tensor = (img_tensor / 255. - 0.5) * 2

        image_tensor_resized = transform(img_tensor) #3,256,256
        videos = image_tensor_resized.unsqueeze(0) # bchw
        
        z = get_latent_z(model, videos.unsqueeze(2)) #bc,1,hw
        
        img_tensor_repeat = repeat(z, 'b c t h w -> b c (repeat t) h w', repeat=frames)

        cond_images = model.embedder(img_tensor.unsqueeze(0)) ## blc
        img_emb = model.image_proj_model(cond_images)

        imtext_cond = torch.cat([text_emb, img_emb], dim=1)

        fs = torch.tensor([fs], dtype=torch.long, device=model.device)
        cond = {"c_crossattn": [imtext_cond], "fs": fs, "c_concat": [img_tensor_repeat]}
        
        ## inference
        batch_samples = batch_ddim_sampling(model, cond, noise_shape, n_samples=1, ddim_steps=steps, ddim_eta=eta, cfg_scale=cfg_scale)
        ## b,samples,c,t,h,w
        prompt_str = prompt.replace("/", "_slash_") if "/" in prompt else prompt
        prompt_str = prompt_str.replace(" ", "_") if " " in prompt else prompt_str
        prompt_str=prompt_str[:40]
        if len(prompt_str) == 0:
            prompt_str = 'empty_prompt'

        save_videos(batch_samples, self.result_dir, filenames=[prompt_str], fps=self.save_fps)
        print(f"Saved in {prompt_str}. Time used: {(time.time() - start):.2f} seconds")
        model = model.cpu()
        return os.path.join(self.result_dir, f"{prompt_str}.mp4")
    
    def download_model(self):
        REPO_ID = 'Doubiiu/DynamiCrafter'
        filename_list = ['model.ckpt']
        if not os.path.exists('./checkpoints/dynamicrafter_256_v1/'):
            os.makedirs('./dynamicrafter_256_v1/')
        for filename in filename_list:
            local_file = os.path.join('./checkpoints/dynamicrafter_256_v1/', filename)
            if not os.path.exists(local_file):
                hf_hub_download(repo_id=REPO_ID, filename=filename, local_dir='./checkpoints/dynamicrafter_256_v1/', local_dir_use_symlinks=False)
    
if __name__ == '__main__':
    i2v = Image2Video()
    video_path = i2v.get_image('prompts/art.png','man fishing in a boat at sunset')
    print('done', video_path)