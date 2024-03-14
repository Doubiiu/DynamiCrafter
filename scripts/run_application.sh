version=$1 # interp or loop
ckpt=checkpoints/dynamicrafter_512_interp_v1/model.ckpt
config=configs/inference_512_v1.0.yaml

prompt_dir=prompts/512_$1/
res_dir="results"

FS=5 ## This model adopts FPS=5, range recommended: 5-30 (smaller value -> larger motion)


if [ "$1" == "interp" ]; then
seed=12306
name=dynamicrafter_512_$1_seed${seed}
CUDA_VISIBLE_DEVICES=0 python3 scripts/evaluation/inference.py \
--seed ${seed} \
--ckpt_path $ckpt \
--config $config \
--savedir $res_dir/$name \
--n_samples 1 \
--bs 1 --height 320 --width 512 \
--unconditional_guidance_scale 7.5 \
--ddim_steps 50 \
--ddim_eta 1.0 \
--prompt_dir $prompt_dir \
--text_input \
--video_length 16 \
--frame_stride ${FS} \
--timestep_spacing 'uniform_trailing' --guidance_rescale 0.7 --perframe_ae --interp
else
seed=234
name=dynamicrafter_512_$1_seed${seed}
CUDA_VISIBLE_DEVICES=0 python3 scripts/evaluation/inference.py \
--seed ${seed} \
--ckpt_path $ckpt \
--config $config \
--savedir $res_dir/$name \
--n_samples 1 \
--bs 1 --height 320 --width 512 \
--unconditional_guidance_scale 7.5 \
--ddim_steps 50 \
--ddim_eta 1.0 \
--prompt_dir $prompt_dir \
--text_input \
--video_length 16 \
--frame_stride ${FS} \
--timestep_spacing 'uniform_trailing' --guidance_rescale 0.7 --perframe_ae --loop
fi
