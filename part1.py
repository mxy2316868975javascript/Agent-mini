
# 导入gradio包
import gradio as gr
import numpy as np
import cv2

# 定义函数, 实现功能
def reverse_text(text):
    return text[::-1]

def hellotoperson(name):
    return '你好' + name

def reverse_and_count(text):
    reverse_text = text[::-1]
    length = len(text)
    return reverse_text, length

def image_to_sketch(image):
    gray_image = image.convert('L')
    inverted_image = 255 - np.array(gray_image)
    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    inverted_blurred = 255 - blurred
    pencil_sketch = cv2.divide(np.array(gray_image), inverted_blurred, scale=256.8)
    return pencil_sketch

# 图片转素描界面配置
demo = gr.Interface(
    fn=image_to_sketch,
    inputs=[gr.Image(label="上传图片",type="pil")],
    outputs=[gr.Image(label="铅笔画")],
    title="图像转铅笔画",
    description="将上传的图片转为铅笔画。"
)

# 界面配置
# demo=gr.Interface(
#     # fn=reverse_text,
#     # fn=hellotoperson,
#     fn=reverse_and_count,
#     inputs="text", # 输入类型为文本
#     # outputs="text" # 输出类型为文本
#     outputs=["text", "number"], # 输出类型为文本, 数字
#     title="文本处理工具", # 设置页面标题
#     description="输入一段文字, 查看其倒序形式及字符数", # 添加简短说明
#     examples=[["你好, 世界"], ["hello world"]]
# )

# 启动应用
demo.launch()