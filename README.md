## ___***DynamiCrafter: Animating Open-domain Images with Video Diffusion Priors***___

<div align="center">

 <a href='https://arxiv.org/abs/2310.12190'><img src='https://img.shields.io/badge/arXiv-2310.12190-b31b1b.svg'></a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
 <a href='https://doubiiu.github.io/projects/DynamiCrafter/'><img src='https://img.shields.io/badge/Project-Page-Green'></a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;



_**[Jinbo Xing](https://doubiiu.github.io/), [Menghan Xia*](https://menghanxia.github.io), [Yong Zhang](https://yzhang2016.github.io), [Haoxin Chen](), [Wangbo Yu](), <br>[Hanyuan Liu](https://github.com/hyliu), [Xintao Wang](https://xinntao.github.io/), [Tien-Tsin Wong*](https://www.cse.cuhk.edu.hk/~ttwong/myself.html), [Ying Shan](https://scholar.google.com/citations?hl=en&user=4oXBp9UAAAAJ&view_op=list_works&sortby=pubdate)**_
<br><br>
(* corresponding authors)

From CUHK and Tencent AI Lab.

</div>
 
## 🔆 Introduction

🤗 DynamiCrafter can animate open-domain still images based on text prompt by leveraging the pre-trained video diffusion priors. Please check our project page and paper for more information. <br>
😀 We will continue to improve the model's performance, which includes offering higher resolution, eliminating watermarks, and enhancing stability.
### 1. Showcases

<table class="center">
    <!-- <tr style="font-weight: bolder;text-align:center;">
        <td>Input</td>
        <td>Output</td>
        <td>Input</td>
        <td>Output</td>
    </tr> -->
  <tr>
    <td colspan="2">"bear playing guitar happily, snowing"</td>
    <td colspan="2">"boy walking on the street"</td>
  </tr>
  <tr>
  <td>
    <img src=assets/showcase/guitar0.jpeg_00.png width="170">
  </td>
  <td>
    <img src=assets/showcase/guitar0.gif width="170">
  </td>
  <td>
    <img src=assets/showcase/walk0.png_00.png width="170">
  </td>
  <td>
    <img src=assets/showcase/walk0.gif width="170">
  </td>
  </tr>


  <tr>
    <td colspan="2">"two people dancing"</td>
    <td colspan="2">"girl talking and blinking"</td>
  </tr>
  <tr>
  <td>
    <img src=assets/showcase/dance1.jpeg_00.png width="170">
  </td>
  <td>
    <img src=assets/showcase/dance1.gif width="170">
  </td>

  <td>
    <img src=assets/showcase/girl3.jpeg_00.png width="170">
  </td>
  <td>
    <img src=assets/showcase/girl3.gif width="170">
  </td>
  </tr>


  <tr>
    <td colspan="2">"zoom-in, a landscape, springtime"</td>
    <td colspan="2">"A blonde woman rides on top of a moving washing machine into the sunset."</td>
  </tr>
  <tr>
  <td>
    <img src=assets/showcase/Upscaled_Aime_Tribolet_springtime_landscape_golden_hour_morning_pale_yel_e6946f8d-37c1-4ce8-bf62-6ba90d23bd93.mp4_00.png width="170">
  </td>
  <td>
    <img src=assets/showcase/Upscaled_Aime_Tribolet_springtime_landscape_golden_hour_morning_pale_yel_e6946f8d-37c1-4ce8-bf62-6ba90d23bd93.gif width="170">
  </td>

  <td>
    <img src=assets/showcase/Upscaled_Alex__State_Blonde_woman_riding_on_top_of_a_moving_washing_mach_c31acaa3-dd30-459f-a109-2d2eb4c00fe2.mp4_00.png width="170">
  </td>
  <td>
    <img src=assets/showcase/Upscaled_Alex__State_Blonde_woman_riding_on_top_of_a_moving_washing_mach_c31acaa3-dd30-459f-a109-2d2eb4c00fe2.gif width="170">
  </td>
  </tr>

  <tr>
    <td colspan="2">"explode colorful smoke coming out"</td>
    <td colspan="2">"a bird on the tree branch"</td>
  </tr>
  <tr>
  <td>
    <img src=assets/showcase/explode0.jpeg_00.png width="170">
  </td>
  <td>
    <img src=assets/showcase/explode0.gif width="170">
  </td>

  <td>
    <img src=assets/showcase/bird000.jpeg width="170">
  </td>
  <td>
    <img src=assets/showcase/bird000.gif width="170">
  </td>
  </tr>
</table >

### 2. Applications
#### 2.1 Storytelling video generation (see project page for more details)
<table class="center">
    <!-- <tr style="font-weight: bolder;text-align:center;">
        <td>Input</td>
        <td>Output</td>
        <td>Input</td>
        <td>Output</td>
    </tr> -->
  <tr>
    <td colspan="4"><img src=assets/application/storytellingvideo.gif width="250"></td>
  </tr>
</table >

#### 2.2 Looping video generation
<table class="center">

  <tr>
  <td>
    <img src=assets/application/60.gif width="300">
  </td>
  <td>
    <img src=assets/application/35.gif width="300">
  </td>
  <td>
    <img src=assets/application/36.gif width="300">
  </td>
  </tr>
  <tr>
  <td>
    <img src=assets/application/05.gif width="300">
  </td>
  <td>
    <img src=assets/application/25.gif width="300">
  </td>
  <td>
    <img src=assets/application/34.gif width="300">
  </td>
  </tr>
</table >

#### 2.3 Generative frame interpolation

<table class="center">
    <tr style="font-weight: bolder;text-align:center;">
        <td>Input starting frame</td>
        <td>Input ending frame</td>
        <td>Generated video</td>
    </tr>
  <tr>
  <td>
    <img src=assets/application/gkxX0kb8mE8_input_start.png width="300">
  </td>
  <td>
    <img src=assets/application/gkxX0kb8mE8_input_end.png width="300">
  </td>
  <td>
    <img src=assets/application/gkxX0kb8mE8.gif width="300">
  </td>
  </tr>

  <tr>
  <td>
    <img src=assets/application/YwHJYWvv_dM_input_start.png width="300">
  </td>
  <td>
    <img src=assets/application/YwHJYWvv_dM_input_end.png width="300">
  </td>
  <td>
    <img src=assets/application/YwHJYWvv_dM.gif width="300">
  </td>
  </tr>

  <tr>
  <td>
    <img src=assets/application/ypDLB52Ykk4_input_start.png width="300">
  </td>
  <td>
    <img src=assets/application/ypDLB52Ykk4_input_end.png width="300">
  </td>
  <td>
    <img src=assets/application/ypDLB52Ykk4.gif width="300">
  </td>
  </tr>
</table >



## 📝 Changelog
- __[2023.11.27]__: 🔥🔥 Launch the project page and update the arXiv preprint.
<br>


## 🧰 Models (will be released within this week)

<!-- |Model|Resolution|Checkpoint|Description
|:---------|:---------|:--------|:--------|
|DynamiCrafter256|256x256|[Hugging Face]()|Support 16 frames -->

<!-- (Reduce the number of frames when you have smaller GPUs, e.g. 256x256 resolutions with 64 frames.) -->

<!-- ## ⚙️ Setup

### Install Environment via Anaconda (Recommended)
```bash
conda create -n freenoise python=3.8.5
conda activate freenoise
pip install -r requirements.txt
``` -->


<!-- ## 💫 Inference (soon) -->


<!-- 1) Download pretrained T2V models via [Hugging Face](https://huggingface.co/VideoCrafter/Text2Video-512-v1/blob/main/model.ckpt), and put the `model.ckpt` in `checkpoints/base_512_v1/model.ckpt`.
2) Input the following commands in terminal.
```bash
  sh scripts/run_text2video_freenoise_512.sh
``` -->

<!-- 1) Download pretrained T2V models via [Hugging Face](https://huggingface.co/VideoCrafter/Text2Video-1024-v1.0/blob/main/model.ckpt), and put the `model.ckpt` in `checkpoints/base_1024_v1/model.ckpt`.
2) Input the following commands in terminal.
```bash
  sh scripts/run_text2video_freenoise_1024.sh
``` -->


## 👨‍👩‍👧‍👦 Crafter Family
[VideoCrafter1](https://github.com/AILab-CVC/VideoCrafter): Framework for high-quality video generation.

[ScaleCrafter](https://github.com/YingqingHe/ScaleCrafter): Tuning-free method for high-resolution image/video generation.

[TaleCrafter](https://github.com/AILab-CVC/TaleCrafter): An interactive story visualization tool that supports multiple characters.  

[LongerCrafter](https://github.com/arthur-qiu/LongerCrafter): Tuning-free method for longer high-quality video generation.  

[MakeYourVideo, might be a Crafter:)](https://doubiiu.github.io/projects/Make-Your-Video/): Video generation/editing with textual and structural guidance.
## 😉 Citation
```bib
@article{xing2023dynamicrafter,
  title={DynamiCrafter: Animating Open-domain Images with Video Diffusion Priors},
  author={Xing, Jinbo and Xia, Menghan and Zhang, Yong and Chen, Haoxin and Yu, Wangbo and Liu, Hanyuan and Wang, Xintao and Wong, Tien-Tsin and Shan, Ying},
  journal={arXiv preprint arXiv:2310.12190},
  year={2023}
}
```


## 📢 Disclaimer
We develop this repository for RESEARCH purposes, so it can only be used for personal/research/non-commercial purposes.
****