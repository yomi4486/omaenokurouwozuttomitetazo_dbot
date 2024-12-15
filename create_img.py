from PIL import Image,ImageDraw,ImageFont
def image_process(base_text:str):
    if len(base_text) > 30:
        return 1
    if not "\n" in base_text:
        base_text = f"{base_text[:14]}\n{base_text[14:]}"

    img = Image.open('main.png')
    font = ImageFont.truetype('LightNovelPOPv2.otf', 40)
    draw = ImageDraw.Draw(img)

    #左上の点のx座標, 左上の点のy座標, 右下の点のx座標, 右下の点のy座標
    it = draw.textbbox((431, 230), base_text,align='center')
    i1 = it[0]
    i2 = it[2]

    l = int(i1)+int(i2)
    x = l / 4

    draw.text((431-x, 230), base_text, 'black',font=font,align='center')
    img.save("result.jpg")
    return 0