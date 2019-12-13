def Capture(device_num, delay=1, window_name='frame'):
    import cv2
    #import os


    cap = cv2.VideoCapture(device_num)

    if not cap.isOpened():
        return

    #os.makedirs(dir_path, exist_ok=True)
    #base_path = os.path.join(dir_path, basename)

    while True:

        ret, frame = cap.read()
        # 表示用(補助線あり)とキャプチャ用の画像を分ける
        edframe = frame

        key = cv2.waitKey(delay) & 0xFF
        if key == ord('c'):
            # 画像切り抜き img[top : bottom, left : right]
            frame = frame[116 : 360, 120 : 524]

            # 切り抜いた画像を上下反転
            frame = cv2.rotate(frame, cv2.ROTATE_180)



            judge(frame)
        elif key == ord('q'):
            break

        # 補助線を引く
        cv2.rectangle(edframe, (120,116), (524,360),(0,0,255),3)
        # 表示
        cv2.imshow(window_name, edframe)

    cv2.destroyWindow(window_name)


def judge(image_file):
    import OK_pasmo2
    import StationName_conv
    import judge


    # 設置駅
    Set_Sta = ('OE', 9) #湘南台

    # 実施振替輸送（ex.JR1号振替→('JR', 1)）
    """
    JR東日本 : 'JR'
    都営地下鉄 : 'Toei'
    東京メトロ : 'TokyoMetro'
    東急電鉄 : 'Tokyu'
    京王電鉄 : 'Keio'
    相模鉄道 : 'Sotetu'
    横浜市営地下鉄 : 'YokohamaSubway'
    多摩都市モノレール : 'TamaMonorail'
    """
    Transfer = ('Tokyu', 1)

    # 定期券面画像
    """
    image_file = "C:/Users/user/Documents/pasmo/"
    image_file += "OE-09_JT-08"
    image_file += ".png"
    """


    ocrList = OK_pasmo2.PasumoOCR(image_file)

    print(ocrList)

    Pass_Route = StationName_conv.CreatePassRoute(ocrList)

    Route_judge = judge.RouteJudge(Pass_Route, Transfer)

    Sta_judge = judge.StationJudge(Transfer, Set_Sta)

    judge.Transport_judge(Route_judge, Sta_judge)


if __name__ == "__main__":
    # (カメラ番号, 保存ディレクトリ,ファイル名)
    Capture(0)