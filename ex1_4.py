import sys
from PIL import Image
import pyocr
import pyocr.builders

# import datetime
tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(0)
tool = tools[0]

txt_names = []

for i in range(1, 6):

    txt_names.append(
        tool.image_to_string(
            Image.open("images/0" + str(i) + ".png"),  # OCRする画像
            lang="jpn",  # 学習済み言語データ
            builder=pyocr.builders.DigitBuilder(tesseract_layout=6),  # 期待される出力のタイプを指定
        )
    )

sum = 0
for j in range(1, 6):
    sum += int(txt_names[j - 1])

print(sum)
#
# with open(“text.txt”, “w”) as f:
# f.writelines(txt)
