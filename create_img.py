from PIL import Image,ImageDraw,ImageFont
from os.path import join, dirname
from dotenv import load_dotenv
import os 

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

from PIL import Image, ImageDraw, ImageFont
import os

from PIL import Image, ImageDraw, ImageFont
import os

def image_process(base_text: str):
    if len(base_text) > 30:
        return 1
    if "\n" not in base_text:
        base_text = [f"{base_text[:8]}",f"{base_text[8:]}"]

    img = Image.open('main.png')
    font = ImageFont.truetype(os.environ.get("FONT_PATH"), 56)
    draw = ImageDraw.Draw(img)

    # Calculate the bounding box of the text
    bbox = draw.textbbox((0, 0), base_text[0], font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Calculate the position to center the text
    x = (img.width - text_width) / 2
    y = (img.height - text_height) / 1.4

    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    draw.text(
        (x, y),
        base_text[0],
        font=font,
        fill='white',
        stroke_width=5,
        stroke_fill='white',
        align='center'
    )
    draw.text(
        (x, y),
        base_text[0],
        font=font,
        fill='#FFFF00',
        stroke_width=2,
        stroke_fill='black',
        align='center'
    )
    if len(base_text[1])!=0:
        two_bbox = draw.textbbox((0, 0), base_text[1], font=font)
        two_text_width = two_bbox[2] - two_bbox[0]
        two_text_height = two_bbox[3] - two_bbox[1]
        two_line_x = (img.width - two_text_width) / 2
        two_line_y = (img.height - two_text_height) / 1.27
        draw.text(
            (two_line_x, two_line_y),
            base_text[1],
            font=font,
            fill='white',
            stroke_width=5,
            stroke_fill='white',
            align='center'
        )
        draw.text(
            (two_line_x, two_line_y),
            base_text[1],
            font=font,
            fill='#FFFF00',
            stroke_width=2,
            stroke_fill='black',
            align='center'
        )
    img.save("result.png")
    return 0

if __name__ == "__main__":
    import sys
    if len(sys.argv) >=2:
        image_process(sys.argv[1])