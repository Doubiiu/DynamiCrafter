name="dynamicrafter_256"

ckpt='checkpoints/dynamicrafter_256_v1/model.ckpt'
config='configs/inference_256_v1.0.yaml'

prompt_dir="prompts/"
res_dir="results"

CUDA_VISIBLE_DEVICES=0 python3 scripts/evaluation/inference.py \
--seed 123 \
--ckpt_path $ckpt \
--config $config \
--savedir $res_dir/$name \
--n_samples 1 \
--bs 1 --height 256 --width 256 \
--unconditional_guidance_scale 7.5 \
--ddim_steps 50 \
--ddim_eta 1.0 \
--prompt_dir $prompt_dir \
--text_input \
--video_length 16 \
--frame_stride 3

## multi-cond CFG: the <unconditional_guidance_scale> is s_txt, <cfg_img> is s_img
#--multiple_cond_cfg --cfg_img 7.5