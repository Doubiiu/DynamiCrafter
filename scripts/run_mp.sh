version=$1 ##1024, 512, 256
seed=123

name=dynamicrafter_$1_mp_seed${seed}

ckpt=checkpoints/dynamicrafter_$1_v1/model.ckpt
config=configs/inference_$1_v1.0.yaml

prompt_dir=prompts/$1/
res_dir="results"

if [ "$1" == "256" ]; then
    H=256
    FS=3  ## This model adopts frame stride=3
elif [ "$1" == "512" ]; then
    H=320
    FS=24 ## This model adopts FPS=24
elif [ "$1" == "1024" ]; then
    H=576
    FS=10 ## This model adopts FPS=10
else
    echo "Invalid input. Please enter 256, 512, or 1024."
    exit 1
fi

# if [ "$1" == "256" ]; then
# CUDA_VISIBLE_DEVICES=2 python3 scripts/evaluation/inference.py \
# --seed 123 \
# --ckpt_path $ckpt \
# --config $config \
# --savedir $res_dir/$name \
# --n_samples 1 \
# --bs 1 --height ${H} --width $1 \
# --unconditional_guidance_scale 7.5 \
# --ddim_steps 50 \
# --ddim_eta 1.0 \
# --prompt_dir $prompt_dir \
# --text_input \
# --video_length 16 \
# --frame_stride ${FS}
# else
# CUDA_VISIBLE_DEVICES=2 python3 scripts/evaluation/inference.py \
# --seed 123 \
# --ckpt_path $ckpt \
# --config $config \
# --savedir $res_dir/$name \
# --n_samples 1 \
# --bs 1 --height ${H} --width $1 \
# --unconditional_guidance_scale 7.5 \
# --ddim_steps 50 \
# --ddim_eta 1.0 \
# --prompt_dir $prompt_dir \
# --text_input \
# --video_length 16 \
# --frame_stride ${FS} \
# --timestep_spacing 'uniform_trailing' --guidance_rescale 0.7
# fi


## multi-cond CFG: the <unconditional_guidance_scale> is s_txt, <cfg_img> is s_img
#--multiple_cond_cfg --cfg_img 7.5
#--loop

## inference using single node with multi-GPUs:
if [ "$1" == "256" ]; then
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python3 -m torch.distributed.launch \
--nproc_per_node=8 --nnodes=1 --master_addr=127.0.0.1 --master_port=23456 --node_rank=0 \
scripts/evaluation/ddp_wrapper.py \
--module 'inference' \
--seed ${seed} \
--ckpt_path $ckpt \
--config $config \
--savedir $res_dir/$name \
--n_samples 1 \
--bs 1 --height ${H} --width $1 \
--unconditional_guidance_scale 7.5 \
--ddim_steps 50 \
--ddim_eta 1.0 \
--prompt_dir $prompt_dir \
--text_input \
--video_length 16 \
--frame_stride ${FS}
else
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python3 -m torch.distributed.launch \
--nproc_per_node=8 --nnodes=1 --master_addr=127.0.0.1 --master_port=23456 --node_rank=0 \
scripts/evaluation/ddp_wrapper.py \
--module 'inference' \
--seed ${seed} \
--ckpt_path $ckpt \
--config $config \
--savedir $res_dir/$name \
--n_samples 1 \
--bs 1 --height ${H} --width $1 \
--unconditional_guidance_scale 7.5 \
--ddim_steps 50 \
--ddim_eta 1.0 \
--prompt_dir $prompt_dir \
--text_input \
--video_length 16 \
--frame_stride ${FS} \
--timestep_spacing 'uniform_trailing' --guidance_rescale 0.7 --perframe_ae
fi