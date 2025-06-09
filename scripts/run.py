version=$1 # interp or loop
ckpt=r"C:\workspace\cs231n\proj\DynamiCrafter\checkpoints\dynamicrafter_256_v1\dynamicrafter_512_interp_v1.ckpt"
config="./configs/inference_512_v1.0.yaml"
prompt_dir="./prompts/512_interp"
res_dir="results"

FS=5 ## This model adopts FPS=5, range recommended: 5-30 (smaller value -> larger motion)
seed=12306 name=dynamicrafter_512_inter_seed12306 
python ./scripts/evaluation/inference.py --seed 12306 --ckpt_path "C:\workspace\cs231n\proj\DynamiCrafter\checkpoints\dynamicrafter_256_v1\dynamicrafter_512_interp_v1.ckpt" --config "./configs/inference_512_v1.0.yaml" --savedir "./results/inter" --n_samples 1  --bs 1 --height 320 --width 512  --unconditional_guidance_scale 7.5  --ddim_steps 50  --ddim_eta 1.0 --prompt_dir "./prompts/512_interp" --text_input --video_length 16 --frame_stride 5 --timestep_spacing 'uniform_trailing' --guidance_rescale 0.7 --perframe_ae --interp