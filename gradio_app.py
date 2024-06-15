import os, argparse
import sys
import gradio as gr
import random
from scripts.gradio.i2v_test import Image2Video
sys.path.insert(1, os.path.join(sys.path[0], 'lvdm'))

i2v_examples_1024 = [
    ['prompts/1024/astronaut04.png', 'a man in an astronaut suit playing a guitar', 50, 7.5, 1.0, 6, 123],
    ['prompts/1024/bloom01.png', 'time-lapse of a blooming flower with leaves and a stem', 50, 7.5, 1.0, 10, 123],
    ['prompts/1024/girl07.png', 'a beautiful woman with long hair and a dress blowing in the wind', 50, 7.5, 1.0, 10, 123],
    ['prompts/1024/pour_bear.png', 'pouring beer into a glass of ice and beer', 50, 7.5, 1.0, 10, 123],
    ['prompts/1024/robot01.png', 'a robot is walking through a destroyed city', 50, 7.5, 1.0, 10, 123],
    ['prompts/1024/firework03.png', 'fireworks display', 50, 7.5, 1.0, 10, 123],
]

i2v_examples_512 = [
    ['prompts/512/bloom01.png', 'time-lapse of a blooming flower with leaves and a stem', 50, 7.5, 1.0, 24, 123],
    ['prompts/512/campfire.png', 'a bonfire is lit in the middle of a field', 50, 7.5, 1.0, 24, 123],
    ['prompts/512/isometric.png', 'rotating view, small house', 50, 7.5, 1.0, 24, 123],
    ['prompts/512/girl08.png', 'a woman looking out in the rain', 50, 7.5, 1.0, 24, 1234],
    ['prompts/512/ship02.png', 'a sailboat sailing in rough seas with a dramatic sunset', 50, 7.5, 1.0, 24, 123],
    ['prompts/512/zreal_penguin.png', 'a group of penguins walking on a beach', 50, 7.5, 1.0, 20, 123],
]

i2v_examples_256 = [
    ['prompts/256/art.png', 'man fishing in a boat at sunset', 50, 7.5, 1.0, 3, 234],
    ['prompts/256/boy.png', 'boy walking on the street', 50, 7.5, 1.0, 3, 125],
    ['prompts/256/dance1.jpeg', 'two people dancing', 50, 7.5, 1.0, 3, 116],
    ['prompts/256/fire_and_beach.jpg', 'a campfire on the beach and the ocean waves in the background', 50, 7.5, 1.0, 3, 111],
    ['prompts/256/girl3.jpeg', 'girl talking and blinking', 50, 7.5, 1.0, 3, 111],
    ['prompts/256/guitar0.jpeg', 'bear playing guitar happily, snowing', 50, 7.5, 1.0, 3, 122]
]

max_seed = 2 ** 31


def dynamicrafter_demo(result_dir='./tmp/', res=1024):
    if res == 1024:
        resolution = '576_1024'
        css = """#input_img {max-width: 1024px !important} #output_vid {max-width: 1024px; max-height:576px} #random_button {max-width: 100px !important}"""
    elif res == 512:
        resolution = '320_512'
        css = """#input_img {max-width: 512px !important} #output_vid {max-width: 512px; max-height: 320px} #random_button {max-width: 100px !important}"""
    elif res == 256:
        resolution = '256_256'
        css = """#input_img {max-width: 256px !important} #output_vid {max-width: 256px; max-height: 256px} #random_button {max-width: 100px !important}"""
    else:
        raise NotImplementedError(f"Unsupported resolution: {res}")
    image2video = Image2Video(result_dir, resolution=resolution)
    with gr.Blocks(analytics_enabled=False, css=css) as dynamicrafter_iface:
        gr.Markdown("<div align='center'> <h1> DynamiCrafter: Animating Open-domain Images with Video Diffusion Priors </span> </h1> \
                      <h2 style='font-weight: 450; font-size: 1rem; margin: 0rem'>\
                        <a href='https://doubiiu.github.io/'>Jinbo Xing</a>, \
                        <a href='https://menghanxia.github.io/'>Menghan Xia</a>, <a href='https://yzhang2016.github.io/'>Yong Zhang</a>, \
                        <a href=''>Haoxin Chen</a>, <a href=''> Wangbo Yu</a>,\
                        <a href='https://github.com/hyliu'>Hanyuan Liu</a>, <a href='https://xinntao.github.io/'>Xintao Wang</a>,\
                        <a href='https://www.cse.cuhk.edu.hk/~ttwong/myself.html'>Tien-Tsin Wong</a>,\
                        <a href='https://scholar.google.com/citations?user=4oXBp9UAAAAJ&hl=zh-CN'>Ying Shan</a>\
                    </h2> \
                     <a style='font-size:18px;color: #000000' href='https://arxiv.org/abs/2310.12190'> [ArXiv] </a>\
                     <a style='font-size:18px;color: #000000' href='https://doubiiu.github.io/projects/DynamiCrafter/'> [Project Page] </a> \
                     <a style='font-size:18px;color: #000000' href='https://github.com/Doubiiu/DynamiCrafter'> [Github] </a> </div>")
        
        #######image2video######
        if res == 1024:
            with gr.Tab(label='Image2Video_576x1024'):
                with gr.Column():
                    with gr.Row():
                        with gr.Column():
                            with gr.Row():
                                i2v_input_image = gr.Image(label="Input Image",elem_id="input_img")
                            with gr.Row():
                                i2v_input_text = gr.Text(label='Prompts')
                            with gr.Row():
                                i2v_eta = gr.Slider(minimum=0.0, maximum=1.0, step=0.1, label='ETA', value=1.0, elem_id="i2v_eta")
                                i2v_cfg_scale = gr.Slider(minimum=1.0, maximum=15.0, step=0.5, label='CFG Scale', value=7.5, elem_id="i2v_cfg_scale")
                            with gr.Row():
                                i2v_steps = gr.Slider(minimum=1, maximum=60, step=1, elem_id="i2v_steps", label="Sampling steps", value=50)
                                i2v_motion = gr.Slider(minimum=5, maximum=20, step=1, elem_id="i2v_motion", label="FPS", value=10)
                            with gr.Row():
                                i2v_seed = gr.Slider(label='Random Seed', minimum=0, maximum=max_seed, step=1, value=123)
                                random_button = gr.Button('\U0001f3b2\ufe0f', elem_id="random_button")
                            random_button.click(
                                fn=lambda: random.randint(0, max_seed),
                                outputs=i2v_seed,
                                queue=False
                            )
                            i2v_end_btn = gr.Button("Generate")
                        # with gr.Tab(label='Result'):
                        with gr.Row():
                            i2v_output_video = gr.Video(label="Generated Video",elem_id="output_vid",autoplay=True,show_share_button=True)

                    gr.Examples(examples=i2v_examples_1024,
                                inputs=[i2v_input_image, i2v_input_text, i2v_steps, i2v_cfg_scale, i2v_eta, i2v_motion, i2v_seed],
                                outputs=[i2v_output_video],
                                fn = image2video.get_image,
                                cache_examples=False,
                    )
                i2v_end_btn.click(inputs=[i2v_input_image, i2v_input_text, i2v_steps, i2v_cfg_scale, i2v_eta, i2v_motion, i2v_seed],
                                outputs=[i2v_output_video],
                                fn = image2video.get_image
                )
        elif res == 512:
            with gr.Tab(label='Image2Video_320x512'):
                with gr.Column():
                    with gr.Row():
                        with gr.Column():
                            with gr.Row():
                                i2v_input_image = gr.Image(label="Input Image",elem_id="input_img")
                            with gr.Row():
                                i2v_input_text = gr.Text(label='Prompts')
                            with gr.Row():
                                i2v_eta = gr.Slider(minimum=0.0, maximum=1.0, step=0.1, label='ETA', value=1.0, elem_id="i2v_eta")
                                i2v_cfg_scale = gr.Slider(minimum=1.0, maximum=15.0, step=0.5, label='CFG Scale', value=7.5, elem_id="i2v_cfg_scale")
                            with gr.Row():
                                i2v_steps = gr.Slider(minimum=1, maximum=60, step=1, elem_id="i2v_steps", label="Sampling steps", value=50)
                                i2v_motion = gr.Slider(minimum=15, maximum=30, step=1, elem_id="i2v_motion", label="FPS", value=24)
                            with gr.Row():
                                i2v_seed = gr.Slider(label='Random Seed', minimum=0, maximum=max_seed, step=1, value=123)
                                random_button = gr.Button('\U0001f3b2\ufe0f', elem_id="random_button")
                            random_button.click(
                                fn=lambda: random.randint(0, max_seed),
                                outputs=i2v_seed,
                                queue=False
                            )
                            i2v_end_btn = gr.Button("Generate")
                        # with gr.Tab(label='Result'):
                        with gr.Row():
                            i2v_output_video = gr.Video(label="Generated Video",elem_id="output_vid",autoplay=True,show_share_button=True)

                    gr.Examples(examples=i2v_examples_512,
                                inputs=[i2v_input_image, i2v_input_text, i2v_steps, i2v_cfg_scale, i2v_eta, i2v_motion, i2v_seed],
                                outputs=[i2v_output_video],
                                fn = image2video.get_image,
                                cache_examples=False,
                    )
                i2v_end_btn.click(inputs=[i2v_input_image, i2v_input_text, i2v_steps, i2v_cfg_scale, i2v_eta, i2v_motion, i2v_seed],
                                outputs=[i2v_output_video],
                                fn = image2video.get_image
                )
        elif res == 256:
            with gr.Tab(label='Image2Video_256x256'):
                with gr.Column():
                    with gr.Row():
                        with gr.Column():
                            with gr.Row():
                                i2v_input_image = gr.Image(label="Input Image",elem_id="input_img")
                            with gr.Row():
                                i2v_input_text = gr.Text(label='Prompts')
                            with gr.Row():
                                i2v_eta = gr.Slider(minimum=0.0, maximum=1.0, step=0.1, label='ETA', value=1.0, elem_id="i2v_eta")
                                i2v_cfg_scale = gr.Slider(minimum=1.0, maximum=15.0, step=0.5, label='CFG Scale', value=7.5, elem_id="i2v_cfg_scale")
                            with gr.Row():
                                i2v_steps = gr.Slider(minimum=1, maximum=60, step=1, elem_id="i2v_steps", label="Sampling steps", value=50)
                                i2v_motion = gr.Slider(minimum=1, maximum=4, step=1, elem_id="i2v_motion", label="Motion magnitude", value=3)
                            with gr.Row():
                                i2v_seed = gr.Slider(label='Random Seed', minimum=0, maximum=max_seed, step=1, value=123)
                                random_button = gr.Button('\U0001f3b2\ufe0f', elem_id="random_button")
                            random_button.click(
                                fn=lambda: random.randint(0, max_seed),
                                outputs=i2v_seed,
                                queue=False
                            )
                            i2v_end_btn = gr.Button("Generate")
                        # with gr.Tab(label='Result'):
                        with gr.Row():
                            i2v_output_video = gr.Video(label="Generated Video",elem_id="output_vid",autoplay=True,show_share_button=True)

                    gr.Examples(examples=i2v_examples_256,
                                inputs=[i2v_input_image, i2v_input_text, i2v_steps, i2v_cfg_scale, i2v_eta, i2v_motion, i2v_seed],
                                outputs=[i2v_output_video],
                                fn = image2video.get_image,
                                cache_examples=False,
                    )
                i2v_end_btn.click(inputs=[i2v_input_image, i2v_input_text, i2v_steps, i2v_cfg_scale, i2v_eta, i2v_motion, i2v_seed],
                                outputs=[i2v_output_video],
                                fn = image2video.get_image
                )
        
    return dynamicrafter_iface

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--res", type=int, default=1024, choices=[1024,512,256], help="select the model based on the required resolution")

    return parser

if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()

    result_dir = os.path.join('./', 'results')
    dynamicrafter_iface = dynamicrafter_demo(result_dir, args.res)
    dynamicrafter_iface.queue(max_size=12)
    dynamicrafter_iface.launch(max_threads=1)
    # dynamicrafter_iface.launch(server_name='0.0.0.0', server_port=80, max_threads=1)