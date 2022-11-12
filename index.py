import pyocr
from PIL import Image
import datetime

tools = pyocr.get_available_tools()
tool = tools[0]


value = 0
for i in range(1, 6):
    img = Image.open("images/0" + str(i) + ".png")
    txt = tool.image_to_string(img, lang="jpn", builder=pyocr.builders.DigitBuilder(tesseract_layout=6))
    value += int(txt)

now = datetime.datetime.now()

print(
    str(now.year)
    + "/"
    + str(now.month)
    + "/"
    + str(now.day)
    + "の摂取カロリーは"
    + str(value)
    + "kcalです。"
)
