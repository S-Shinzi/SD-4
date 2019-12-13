def JudgeManager(image_file):
    import OK_pasmo
    import StationName_conv
    import judge
    import cv2


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
    image_file = "C:/Users/user/Documents/pasmo/"
    image_file += "OE-09_JT-08"
    image_file += ".png"

    img = cv2.imread(image_file)

    ocrList = OK_pasmo.PasumoOCR(img)

    Pass_Route = StationName_conv.CreatePassRoute(ocrList)

    Route_judge = judge.RouteJudge(Pass_Route, Transfer)

    Sta_judge = judge.StationJudge(Transfer, Set_Sta)

    judge.Transport_judge(Route_judge, Sta_judge)