#   Pil和Pillow不能同时存在,下面使用的是Pillow模块.
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
#   自动换行模块
import textwrap
#   文本样式
import pandas as pd
import xlrd
#   表格处理模块
#   text_name = str(input("输入名称："))


def excel_num():
    #   获取表格数据
    num = pd.read_excel("C:/name1.xlsx")
    text_name = num["A"][0]
    #   得到表格第一列第0个值给到 text_name
    return text_name


def Image_io(text_name):
    #   获取图片
    im = Image.open("999.png")

    #   获取字体和字号值
    myfont = ImageFont.truetype("C:/r.ttf", size=55)

    #   使用此模块创建新图像
    draw = ImageDraw.Draw(im)

    #   写入坐标，换行，内容，字色，变量
    draw.text((446, 906), textwrap.fill(text_name, width=10),  fill=(251, 198, 0), font=myfont)

    #   显示此图像。此方法主要用于调试目的。
    im.show()

    #   输出图片
    im.save('new.png')


if __name__ == '__main__':
    text_name = excel_num()
    print(text_name)
    Image_io(text_name)