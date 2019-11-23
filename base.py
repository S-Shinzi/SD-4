# -*- coding:utf-8 -*-
import tkinter as tk
import tkinter.ttk as ttk
import numpy as np
import cv2
from PIL import Image, ImageTk
import sys
import pyocr
import pyocr.builders#pyocrを2列にする必要があるかはわからないが、精度が落ちると嫌なので一応書いておく
import time
#import"文字読み取り"

root = tk.Tk()
root.title("定期")
root['background'] ='gray'

root2 = tk.Tk()
root2.title("テキスト")
root2['background'] ='gray'


listn = ["AA","BB","CC"]
print(listn)

def delsan(event):
    del listn[0:3]
    print(listn)
    arai(event)
def teiki(event):
    count = 0
    t1 = time.time() 
    image_file = "smkt.png"#まず、ここで読み取った画像を指定する
    img = cv2.imread(image_file)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([0, 0, 0])    #色の情報。ここから、↓
    upper = np.array([150, 200, 200])#ここまでの範囲を指定することで、青い文字以外を指定する。
    img_mask = cv2.inRange(hsv, lower, upper)
    img_color = cv2.bitwise_and(img, img, mask=img_mask)#おそらく、ここで背景（上の範囲指定、白背景と乗り物マークを含む）を黒くしている


    cv2.imwrite("end.png", img_color)#ここで背景の黒い画像を保存して、
    img = cv2.imread("end.png")#ここで背景の黒い画像を呼び出す。ここの処理がないと現状うまく画像ができない。


    white_pixels = (img == (0, 0, 0)).all(axis=-1)#背景の黒色を(0, 0, 0)、と指定
    img[white_pixels] = (241,242,242)#ここで黒色(0, 0, 0)の範囲を背景の色(241,242,242)に、変更している。
    cv2.imwrite("end.png", img)#おそらく、ここで変更された画像をセーブしている。

    #//ここまでで背景（青文字以外）を白色にする処理がされる//


    # ここからは、うえの９行目～でやっている背景を黒くする処理と同じで、
    image_file = 'end.png'#青文字のみを指定して、黒文字にしている
    img = cv2.imread(image_file)

    # detect pink 
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([0, 0, 0])    #真っ黒
    upper = np.array([150, 150, 250])#(現状)青の文字のみが読み取れる範囲指定
    img_mask = cv2.inRange(hsv, lower, upper)
    img_color = cv2.bitwise_and(img, img, mask=img_mask)

    # debug
    cv2.imwrite("end.png", img_color)#黒文字になったのを保存。これで画像が完成。



    tools = pyocr.get_available_tools()#ここからはpyocrを用いた文字認識の処理となる。

    if len(tools) == 0:#文字認識の環境ができていない場合は、ここで　No OCR tool found　の文字が出てくるようにする。
        print("No OCR tool found")
        sys.exit(1)

    tool = tools[0]

    img = cv2.imread("end.png", cv2.IMREAD_GRAYSCALE)


    #座標の指定は x, y, width, Height
    box_area = np.array( [[72, 142, 348, 65],   #京王八王子
                        [614, 149, 279, 65],  #下北沢
                        [127, 229, 108, 39],  #明大前　　の文字がある座標を指定。 
                        ])  #これをすることで文字認識の精度がかなり上がる。

    for box in box_area:#box_areaの数だけループする。指定したい場合は、レンジ？で指定する。
        #イメージは OpenCV -> PIL に変換する←　よくわからないけど重要そうなメモ
        txt = tool.image_to_string(Image.fromarray(img[box[1]:box[1]+box[3], box[0]:box[0]+box[2]]), lang="jpn", builder=pyocr.builders.TextBuilder(tesseract_layout=7))
        #↑で、日本語で処理をするとか、いろいろと設定をしている
        print(txt)#ここで読み取り結果を表示するようになっている。txtboxを試す
        count += 20
        print(count)
        #label2 = tk.Label(root2,text=txt) "#   ここから３つはテスト用、消してもよし
        #label2.grid()                                #tkを持ったlabelをウィンドウに表示
        #label2.place(x=0, y= count + 20)
        text_widget.insert('1.0', txt+'\n')
        listn.append(txt)
        print(listn)

    # 計測したい処理
    for i in range(1000000):
        i ** 10
    
    # 処理後の時刻
    t2 = time.time()
    
    # 経過時間を表示
    elapsed_time = t2-t1
    print(f"経過時間：{elapsed_time}")


def arai(event):
    print("実行")


    # 画像を表示するための準備
    img = Image.open('smkt.png')


    img_resize_lanczos = img.resize((290, 250), Image.LANCZOS)
    img_resize_lanczos.save('sumokita.png')
    img = Image.open('sumokita.png')#サイズ変更と保存

    img = ImageTk.PhotoImage(img)
    # 画像を表示するためのキャンバスの作成（青で表示）
    canvas = tk.Canvas(bg = "blue", width=280, height=240)
    canvas.place(x=30, y=30) # 左上の座標を指定
    # キャンバスに画像を表示する。第一引数と第二引数は、x, yの座標
    canvas.create_image(0, 0, image=img, anchor=tk.NW)

    teiki(event)# 画像を表示するための準備
    root.mainloop()#これがないとがぞうが表示されん。ウィンドウ作業完了の合図みたいなもんみたい



    



for i in range(1):                              #ボタンの数は１こ
    root.geometry("800x600+0+20")              #winサイズと位置設定
    
        # ボタン、ウィンドウの設定
    button = tk.Button(root,text="判定")#ボタンの名前はダイスロール

        # ウィジェットが左クリックされたときの関数を定義
    
    button.bind("<1>",delsan)     
            
                #ボタンが押されることによってcallbackに飛ぶ
        # ボタンとテキストの配置
    button.place(x=40,y=2)                      #ウィンドウ内ボタンの位置
    label1 = tk.Label(root,text="label1 テキストが入れられます")        #tk(乱数)をセット
    label1.grid()                                #tkを持ったlabelをウィンドウに表示
    label1.place(x=80, y=80)
    combo = ttk.Combobox(root, state='readonly')
    combo2 = ttk.Combobox(root, state='readonly')
    # リストの値を設定
    combo["values"] = ("JR1号","辻堂駅","藤沢駅")
    combo2["values"] = ("湘南台駅","駅名","駅")
        # デフォルトの値を食費(index=0)に設定
    combo.current(0)
    combo2.current(0)
    # コンボボックスの配置
    combo.pack()
    combo2.pack()
    # ボタンの作成（コールバックコマンドには、コンボボックスの値を取得しprintする処理を定義）
    button = tk.Button(text="表示",command=lambda:print(combo.get()+"\n",combo2.get()))#\nで改行,それぞれのcomboの値を表示
    # ボタンの配置
    button.pack()

    root2.geometry("300x600+800+20")              #winサイズと位置設定
    
        # ボタン、ウィンドウの設定

        # ウィジェットが左クリックされたときの関数を定義
                        #ウィンドウ内ボタンの位置
    labelA = tk.Label(root2,text="labelA テキストが入れられます")        #tk(乱数)をセット
    labelA.grid()                                #tkを持ったlabelをウィンドウに表示
    labelA.place(x=500, y=500)
    # 画面タイトル

    root2.title('Editor Test')

    text_widget = tk.Text(root2)
    text_widget.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))

    root2.columnconfigure(0, weight=1)
    root2.rowconfigure(0, weight=1)
    root2.mainloop()



root.mainloop()