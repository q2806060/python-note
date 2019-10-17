import pytesseract
# Python图像处理标准库
from PIL import Image

# 创建图片对象
img = Image.open("test2.jpg")

# 图片转字符串
result = pytesseract.image_to_string(img)
print(result)