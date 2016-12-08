
# coding: utf-8
import Image, ImageDraw, ImageFont, ImageFilter
import string, random

fontType = "/usr/share/fonts/truetype/freefont/FreeSans.ttf"


# 获得随机四个字母
def getRandomChar():
    source = list(string.letters)
    for index in range(0, 10):
        source.append(str(index))


    return ''.join(random.sample(source, 4))



# 获得颜色
def getRandomColor():

    return (random.randint(30, 255), random.randint(30, 200), random.randint(30, 200))


# 获得验证码图片
def getCodePiture(font_type=fontType):
    width = 240
    height = 60
    # 创建画布
    image = Image.new('RGB', (width, height), (180, 180, 180))
    font = ImageFont.truetype(font_type, 40)
    draw = ImageDraw.Draw(image)
    # 创建验证码对象
    code = getRandomChar()
    print code
    # 把验证码放到画布上
    for t in range(4):

        draw.text((60 * t + 10, 0), code[t],font=font, fill=getRandomColor())
    # 填充噪点
    for _ in range(random.randint(1500, 3000)):
        draw.point((random.randint(0, width), random.randint(0, height)), fill=getRandomColor())
    # 模糊处理
    image = image.filter(ImageFilter.BLUR)
    # 保存名字为验证码的图片
    # image.save("".join(code) + '.jpg', 'jpeg');
    image.save("./img/topian.gif", "GIF")

if __name__ == '__main__':
    getCodePiture()


