import cv2
import gradio as gr

# 模板图片路径
template_images = {
    "Lena": "template/Lena.png",
    "OpenCV": "template/opencv_logo.png"
}

def process_image(image, threshold=128):
    # 如果输入是None，返回None
    if image is None:
        return None, None
    # 转为灰度
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 自适应阈值二值化
    binary = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        cv2.THRESH_BINARY, 11, 2
    )
    return gray, binary

def infer(input_image, threshold):
    if input_image is None:
        return None, None
    gray, binary = process_image(input_image, threshold)
    return gray, binary



with gr.Blocks() as gradio:
    gr.Markdown("## 图片灰度化与二值化演示")
    with gr.Row():
        with gr.Column():
            image_input = gr.Image(label="上传图片或点击下方模板", type="numpy")
            gr.Markdown("#### 模板")
            with gr.Row():
                lena_img = cv2.imread(template_images["Lena"])
                lena_img = cv2.cvtColor(lena_img, cv2.COLOR_BGR2RGB) if lena_img is not None else None
                opencv_img = cv2.imread(template_images["OpenCV"])
                opencv_img = cv2.cvtColor(opencv_img, cv2.COLOR_BGR2RGB) if opencv_img is not None else None
                lena = gr.Image(value=lena_img, label="Lena", interactive=False, show_label=True, elem_id="lena_template", height=100)
                opencv = gr.Image(value=opencv_img, label="OpenCV", interactive=False, show_label=True, elem_id="opencv_template", height=100)
            threshold_slider = gr.Slider(0, 255, value=128, label="二值化阈值")
            btn = gr.Button("处理")
        with gr.Column():
            gray_output = gr.Image(label="灰度图")
            binary_output = gr.Image(label="二值图")

    def set_input_lena():
        return gr.update(value=lena_img)
    def set_input_opencv():
        return gr.update(value=opencv_img)

    lena.select(fn=set_input_lena, inputs=None, outputs=image_input)
    opencv.select(fn=set_input_opencv, inputs=None, outputs=image_input)

    btn.click(
        fn=infer,
        inputs=[image_input, threshold_slider],
        outputs=[gray_output, binary_output]
    )

if __name__ == "__main__":
    gradio.launch()