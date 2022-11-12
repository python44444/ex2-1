import pyocr
from PIL import Image
import datetime

tools = pyocr.get_available_tools()
tool = tools[0]


def ocr():
    number = 0
    for i in range(1, 6):
        img = Image.open("images/0" + str(i) + ".png")
        txt = tool.image_to_string(
            img, lang="jpn", builder=pyocr.builders.DigitBuilder(tesseract_layout=6)
        )
        number += int(txt)
    return number


def save(text):
    with open("ex1.txt", "w") as f:
        f.write(str(text))


def display():
    value = ocr()
    save(value)
    f = open("ex1.txt", "r", encoding="UTF-8")
    out = f.read()

    now = datetime.datetime.now()
    print(
        str(now.year)
        + "/"
        + str(now.month)
        + "/"
        + str(now.day)
        + "の摂取カロリーは"
        + str(out)
        + "kcalです。"
    )


display()
