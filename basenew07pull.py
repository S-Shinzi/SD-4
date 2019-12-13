# -*- coding:utf-8 -*-
import tkinter as tk
import tkinter.ttk as ttk
import tkinter as tki
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
import sys
import threading#カメラ関係、必須

#！！！最初に読んで下さい！！！
#現段階では、ウィンドウを消してもターミナルが消えず、カメラが起動したになってしまっています。
#VScode等で実行してしまった場合、VScodeのウィンドウを消さないとターミナル及びカメラが終了しないので
#起動する際はファイルを直接ダブルクリック等して起動することをお勧めします。


#import"文字読み取り"

root = tk.Tk()
root.title("定期")
root['background'] ='gray'
root.bind('<Escape>', lambda e: root.quit())
root.geometry("1000x600+0+20")
root.resizable(width=False, height=False)
#root.protocol('WM_DELETE_WINDOW', doSomething)  #ここに、右上X関係の処理のヒントがあります


lmain = tk.Label(root)
lmain.grid()


def on_closing():
    ret = messagebox.askyesno('確認', 'ウィンドウを閉じますか？')
    if ret == True:
        sys.exit()
    
root.protocol("WM_DELETE_WINDOW", on_closing)

def crozz(event):
    sys.exit()




def videoLoop(mirror=False):
    No=0
    cap = cv2.VideoCapture(No)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 10)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1)

    while True:
        ret, frame = cap.read()
        if mirror is True:
            frame = frame[:,::-1]

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
        panel = tk.Label(image=image, width=291, height=245)
        panel.image = image
        panel.place(x=325, y=35)

    return panel




def dow():

    canvas01 = tk.Canvas(root, width=2800, height=2450)
    canvas01.create_rectangle(0, 0, 2800, 2450, fill='gray')
    canvas01.place(x=0, y=0)

    canvas01b = tk.Canvas(root, width=290, height=255)
    canvas01b.create_rectangle(0, 0, 949,333, fill='black')
    canvas01b.place(x=10, y=30)
    canvas01 = tk.Canvas(root, width=280, height=245)
    canvas01.create_rectangle(0, 0, 0, 0, fill='white')
    canvas01.place(x=15, y=35)


    canvas02b = tk.Canvas(root, width=302, height=255)
    canvas02b.create_rectangle(0, 0, 949,333, fill='black')
    canvas02b.place(x=320, y=30)
    canvas02 = tk.Canvas(root, width=292, height=245)
    canvas02.create_rectangle(0, 0, 0, 0, fill='white')
    canvas02.place(x=325, y=35)




    canvas03b = tk.Canvas(root, width=310, height=365)
    canvas03b.create_rectangle(0, 0, 310,365, fill='black')
    canvas03b.place(x=645, y=30)
    canvas03 = tk.Canvas(root, width=300, height=355)
    canvas03.create_rectangle(0, 0, 0, 0, fill='gray')
    canvas03.place(x=650, y=35)

    canvas02b = tk.Canvas(root, width=611, height=100)
    canvas02b.create_rectangle(0, 0, 949,333, fill='black')
    canvas02b.place(x=10, y=295)
    canvas02 = tk.Canvas(root, width=601, height=90)
    canvas02.create_rectangle(0, 0, 0, 0, fill='gray')
    canvas02.place(x=15, y=300)

    canvas05b = tk.Canvas(root, width=948, height=170)
    canvas05b.create_rectangle(0, 0, 949,199, fill='black')
    canvas05b.place(x=10, y=420)
    canvas02 = tk.Canvas(root, width=938, height=160)
    canvas02.create_rectangle(0, 0, 0, 0, fill='gray')
    canvas02.place(x=15, y=425)

    labela = tk.Label(root,text="振り替え情報")        #tk(乱数)をセット
    labela.place(x = 700,y = 80)  # rowspan=1 行感覚                            #tkを持ったlabelをウィンドウに表示

    labelb = tk.Label(root,text="設置駅")        #tk(乱数)をセット
    #labelb.grid(column=50, row=3,pady=10)                  #tkを持ったlabelをウィンドウに表示
    labelb.place(x = 700,y = 200)

    labelt = tk.Label(root,text="設定")        #tk(乱数)をセット                              #tkを持ったlabelをウィンドウに表示
    labelt.place(x = 700,y = 50)
    #label1 = tk.Label(root,text="label1 テキストが入れられます")        #tk(乱数)をセット
    #label1.grid()                                #tkを持ったlabelをウィンドウに表示
    #label1.place(x=602, y=80)

dow()

listn = ["AA","BB","CC"]
print(listn)

def delsan(event):
    del listn[0:3]
    print(listn)
    arai(event)

def popup(event):
    print("簡易メッセージ、エラーが出ました") 
    txt3.insert('1.0', "簡易メッセージ、エラーが出ました"+'\n')  
    messagebox.showerror("エラー", "ここにエラーメッセージを記入")
    #txt2.showinfo(title="Greetings", message="エラー!") 

class App(object):

    def __init__(self):
        self.root = tki.Tk()

    # create a Frame for the Text and Scrollbar
        txt_frm = tki.Frame(self.root, width=600, height=600)
        txt_frm.pack(fill="both", expand=True)
        # ensure a consistent GUI size
        txt_frm.grid_propagate(False)
        # implement stretchability
        txt_frm.grid_rowconfigure(0, weight=1)
        txt_frm.grid_columnconfigure(0, weight=1)

    # create a Text widget
        self.txt = tki.Text(txt_frm, borderwidth=3, relief="sunken")
        self.txt.config(font=("consolas", 12), undo=True, wrap='word')
        self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

    # create a Scrollbar and associate it with txt
        scrollb = tki.Scrollbar(txt_frm, command=self.txt.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = scrollb.set


def win2(event):
    app = App()
    app.root.mainloop()


for i in range(1):                              #ボタンの数は１こ
              #winサイズと位置設定

    button2 = tk.Button(root,text="エラーテスト")
    button2.bind("<1>",popup)
    button2.place(x=10, y=400)   


    combo = ttk.Combobox(root, state='readonly')
    combo2 = ttk.Combobox(root, state='readonly')
    # リストの値を設定
    combo["values"] = ("JR1号","JR2号","JR3号","JR4号","JR5号","JR6号","JR7号","JR8号","JR9号","JR10号",
    "都営地下鉄1号","都営地下鉄2号","都営地下鉄3号","都営地下鉄4号","都営地下鉄5号","都営地下鉄6号","都営地下鉄7号",
    "東京メトロ1号","東京メトロ2号","東京メトロ5号","東京メトロ9号","東京メトロ20号",
    "東急1号","東急2号","京王1号","相鉄","横浜市営地下鉄線","多摩モノレール")
    combo2["values"] = (
"OH01　新宿駅"
,"OH02　南新宿駅"
,"OH03　参宮橋駅"
,"OH04　代々木八幡駅"
,"OH05　代々木上原駅"
,"OH06　東北沢駅"
,"OH07　下北沢駅"
,"OH08　世田谷代田駅"
,"OH09　梅が丘駅"
,"OH10　豪徳寺駅"
,"OH11　経堂駅"
,"OH12　千歳船橋駅"
,"OH13　祖師ヶ谷大蔵駅"
,"OH14　成城学園前駅"
,"OH15　喜多見駅"
,"OH16　狛江駅"
,"OH17　和泉多摩川駅"
,"OH18　登戸駅"
,"OH19　向ヶ丘遊園駅"
,"OH20　生田駅"
,"OH21　読売ランド前駅"
,"OH22　百合ヶ丘駅"
,"OH23　新百合ヶ丘駅"
,"OH24　柿生駅"
,"OH25　鶴川駅"
,"OH26　玉川学園前"
,"OH27　町田駅"
,"OH28　相模大野駅"
,"OH29　小田急相模原駅"
,"OH30　相武台前駅"
,"OH31　座間駅"
,"OH32　海老名駅"
,"OH33　厚木駅"
,"OH34　本厚木駅"
,"OH35　愛甲石田駅"
,"OH36　伊勢原駅"
,"OH37　鶴巻温泉駅"
,"OH38　東海大学前駅"
,"OH39　秦野駅"
,"OH40　渋沢駅"
,"OH41　新松田駅"
,"OH42　開成駅"
,"OH43　栢山駅"
,"OH44　富水駅"
,"OH45　螢田駅"
,"OH46　足柄駅"
,"OH47　小田原駅"
,"OH48　箱根板橋駅"
,"OH49　風祭駅"
,"OH50　入生田駅"
,"OH51　箱根湯本駅"

,"OE01　東林間駅"
,"OE02　中央林間駅"
,"OE03　南林間駅"
,"OE04　鶴間駅"
,"OE05　大和駅"
,"OE06　桜ヶ丘駅"
,"OE07　高座渋谷駅"
,"OE08　長後駅"
,"OE09　湘南台駅"
,"OE10　六会日大前駅"
,"OE11　善行駅"
,"OE12　藤沢本町駅"
,"OE13　藤沢駅"
,"OE14　本鵠沼駅"
,"OE15　鵠沼海岸駅"
,"OE16　片瀬江ノ島駅"

,"OT01　五月台駅"
,"OT02　栗平駅"
,"OT03　黒川駅"
,"OT04　はるひ野駅"
,"OT05　小田急永山駅"
,"OT06　小田急多摩センター駅"
,"OT07　唐木田駅"

,"C01　代々木上原駅"
,"C02　代々木公園駅"
,"C03　明治神宮前（原宿）駅"
,"C04　表参道駅"
,"C05　乃木坂駅"
,"C06　赤坂駅"
,"C07　国会議事堂前駅"
,"C08　霞が関駅"
,"C09　日比谷駅"
,"C10　二重橋前（丸の内）駅"
,"C11　大手町駅"
,"C12　新御茶ノ水駅"
,"C13　湯島駅"
,"C14　根津駅"
,"C15　千駄木駅"
,"C16　西日暮里駅"
,"C17　町屋駅"
,"C18　北千住駅"
,"C19　綾瀬駅"
,"C20　北綾瀬駅"
,"JL19　綾瀬駅"
,"JL20　亀有駅"
,"JL21　金町駅"
,"JL22　松戸駅"
,"JL23　北松戸駅"
,"JL24　馬橋駅"
,"JL25　新松戸駅"
,"JL26　北小金駅"
,"JL27　南柏駅"
,"JL28　柏駅"
,"JL29　北柏駅"
,"JL30　我孫子駅"
,"JL31　天皇台駅"
,"JL32　取手駅"


)
#pack
    combo.grid(column=50, row=0 )
    combo2.grid(column=50, row=1)
        # デフォルトの値を食費(index=0)に設定
    combo.current(0)
    combo2.current(0)
    # コンボボックスの配置
    combo.grid()
    combo.place(x=700, y=120)
    combo2.grid()
    combo2.place(x=700, y=240)
    # ボタンの作成（コールバックコマンドには、コンボボックスの値を取得しprintする処理を定義）
    button3 = tk.Button(text="ターミナルに表示",command=lambda:print(combo.get()+"\n",combo2.get()))#\nで改行,それぞれのcomboの値を表示
    button4 = tk.Button(root,text="ウィンドウ生成")
    button4.bind("<1>",win2) 
    # ボタンの配置
    button3.grid(column=50, row=20)
    button3.place(x=700, y=300)
    button4.grid(column=50, row=20)
    button4.place(x=820, y=300)


#width=935, height=150)

    root.title('Editor Test')

    text_widget = tk.Text(root, width=86, height=7)
    text_widget.grid()
    text_widget.place(x=15, y=300)
    #text_widget.pack(column=30, row=10, sticky=(tk.N, tk.S, tk.E, tk.W))


    # Frame
    frame1 = ttk.Frame(root, padding=3)
    frame1.rowconfigure(1, weight=1)
    frame1.columnconfigure(0, weight=1)
    frame1.grid()
    frame1.place(x=15, y=300)
    

    # Text
    f = Font(family='Helvetica', size=11)
    v1 = StringVar()
    txt2 = Text(frame1, width=72, height=5)
    txt2.configure(font=f)
    txt2.insert(1.0, "読み取り結果表示")
    txt2.grid(row=1, column=0)
    

    scrollbar = ttk.Scrollbar(
        frame1, 
        orient=VERTICAL, 
        command=txt2.yview)
    txt2['yscrollcommand'] = scrollbar.set
    scrollbar.grid(row=1,column=1,sticky=(N,S))
    




    #text_widget.pack(column=30, row=10, sticky=(tk.N, tk.S, tk.E, tk.W))


    # Frame
    frame2 = ttk.Frame(root, padding=3)
    frame2.rowconfigure(1, weight=1)
    frame2.columnconfigure(0, weight=1)
    frame2.grid()
    frame2.place(x=16, y=426)
    

    # Text
    f2 = Font(family='Helvetica', size=11)
    v1 = StringVar()
    txt3 = Text(frame2, width=114, height=9)
    txt3.configure(font=f2)
    txt3.insert(1.0, "エラー原因表示")
    txt3.grid(row=1, column=0)
    

    scrollbar = ttk.Scrollbar(
        frame2, 
        orient=VERTICAL, 
        command=txt3.yview)
    txt3['yscrollcommand'] = scrollbar.set
    scrollbar.grid(row=1,column=1,sticky=(N,S))





    #text_widgetD = tk.Text(root,width=42, height=19)
    #text_widgetD.place(x=324, y=34)
    #text_widget.pack(column=30, row=10, sticky=(tk.N, tk.S, tk.E, tk.W))



    thread = threading.Thread(target=videoLoop, args=())
    thread.start()



    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.mainloop()






root.mainloop()
sys.exit()