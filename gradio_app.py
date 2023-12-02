import os
import sys
import gradio as gr
from scripts.gradio.i2v_test import Image2Video
sys.path.insert(1, os.path.join(sys.path[0], 'lvdm'))


i2v_examples = [
    ['prompts/art.png', 'man fishing in a boat at sunset', 50, 7.5, 1.0, 3, 234],
    ['prompts/boy.png', 'boy walking on the street', 50, 7.5, 1.0, 3, 125],
    ['prompts/dance1.jpeg', 'two people dancing', 50, 7.5, 1.0, 3, 116],
    ['prompts/fire_and_beach.jpg', 'a campfire on the beach and the ocean waves in the background', 50, 7.5, 1.0, 3, 111],
    ['prompts/girl3.jpeg', 'girl talking and blinking', 50, 7.5, 1.0, 3, 111],
    ['prompts/guitar0.jpeg', 'bear playing guitar happily, snowing', 50, 7.5, 1.0, 3, 111],
]
css = """#input_img {max-width: 256px !important} #output_vid {max-width: 256px; max-height: 256px}"""

def dynamicrafter_demo(result_dir='./tmp/'):
    
    image2video = Image2Video(result_dir)
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
        with gr.Tab(label='Image2Video'):
            with gr.Column():
                with gr.Row():
                    with gr.Column():
                        with gr.Row():
                            i2v_input_image = gr.Image(label="Input Image",elem_id="input_img")
                        with gr.Row():
                            i2v_input_text = gr.Text(label='Prompts')
                        with gr.Row():
                            i2v_seed = gr.Slider(label='Random Seed', minimum=0, maximum=10000, step=1, value=123)
                            i2v_eta = gr.Slider(minimum=0.0, maximum=1.0, step=0.1, label='ETA', value=1.0, elem_id="i2v_eta")
                            i2v_cfg_scale = gr.Slider(minimum=1.0, maximum=15.0, step=0.5, label='CFG Scale', value=7.5, elem_id="i2v_cfg_scale")
                        with gr.Row():
                            i2v_steps = gr.Slider(minimum=1, maximum=60, step=1, elem_id="i2v_steps", label="Sampling steps", value=50)
                            i2v_motion = gr.Slider(minimum=1, maximum=4, step=1, elem_id="i2v_motion", label="Motion magnitude", value=3)
                        i2v_end_btn = gr.Button("Generate")
                    # with gr.Tab(label='Result'):
                    with gr.Row():
                        i2v_output_video = gr.Video(label="Generated Video",elem_id="output_vid",autoplay=True,show_share_button=True)

                gr.Examples(examples=i2v_examples,
                            inputs=[i2v_input_image, i2v_input_text, i2v_steps, i2v_cfg_scale, i2v_eta, i2v_motion, i2v_seed],
                            outputs=[i2v_output_video],
                            fn = image2video.get_image,
                            cache_examples=os.getenv('SYSTEM') == 'spaces',
                )
            i2v_end_btn.click(inputs=[i2v_input_image, i2v_input_text, i2v_steps, i2v_cfg_scale, i2v_eta, i2v_motion, i2v_seed],
                            outputs=[i2v_output_video],
                            fn = image2video.get_image
            )

    return dynamicrafter_iface

if __name__ == "__main__":
    result_dir = os.path.join('./', 'results')
    dynamicrafter_iface = dynamicrafter_demo(result_dir)
    dynamicrafter_iface.queue(max_size=12)
    dynamicrafter_iface.launch(max_threads=1)
    # dynamicrafter_iface.launch(server_name='0.0.0.0', server_port=80, max_threads=1)