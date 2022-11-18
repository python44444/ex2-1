import pyocr
from PIL import Image
import datetime
import os  # module to controll files or directories

tools = pyocr.get_available_tools()
tool = tools[0]


def ocr():
    dir_name = "./images"
    files = os.listdir(r"./images")
    value = 0

    for file in files:
        img = Image.open(os.path.join(dir_name, file))
        txt = tool.image_to_string(
            img, lang="jpn", builder=pyocr.builders.DigitBuilder(tesseract_layout=6)
        )
        value += int(txt)

    return value


def save(text):
    with open("ex1.txt", "w") as f:
        f.write(str(text))


def display():
    value = ocr()
    save(value)

    f = open("ex1.txt", "r", encoding="UTF-8")
    out = f.read()

    today = datetime.date.today()
    date = today.strftime("%Y/%m/%d")

    print(str(date) + "の摂取カロリーは" + str(out) + "kcalです。")


display()
