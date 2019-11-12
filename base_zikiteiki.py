import numpy as np
import cv2
from PIL import Image
import sys
import pyocr
import pyocr.builders#pyocrを2列にする必要があるかはわからないが、精度が落ちると嫌なので一応書いておく



tools = pyocr.get_available_tools()#ここからはpyocrを用いた文字認識の処理となる。

if len(tools) == 0:#文字認識の環境ができていない場合は、ここで　No OCR tool found　の文字が出てくるようにする。
    print("No OCR tool found")
    sys.exit(1)

tool = tools[0]

img = cv2.imread("img_0_m[1].png", cv2.IMREAD_GRAYSCALE)


#座標の指定は x, y, width, Height
box_area = np.array( [[35, 83, 184, 67],   #新宿
                     [319, 88, 192, 56],  #祖師ケ谷大蔵　の文字がある座標を指定。 
                    ])  #これをすることで文字認識の精度がかなり上がる。

for box in box_area:
    #イメージは OpenCV -> PIL に変換する←　よくわからないけど重要そうなメモ
    txt = tool.image_to_string(Image.fromarray(img[box[1]:box[1]+box[3], box[0]:box[0]+box[2]]), lang="jpn", builder=pyocr.builders.TextBuilder(tesseract_layout=7))
    #↑で、日本語で処理をするとか、いろいろと設定をしている
    print(txt)#ここで読み取り結果を表示するようになっている。