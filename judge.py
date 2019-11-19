# mysqlclient-1.4.5


# 振替輸送情報の変換
def Transfer_conv(Transfer):
    if Transfer == ('JR', 10):
        return ((1,18),(0,0),(0,0))
    elif Transfer[0] == 'JR' or 'Sotetu' or 'Toei':
        return ((1,47),(1,16),(1,7))
    elif Transfer[0] == 'ToykoMetoro':
        return ((1,7),(0,0),(0,0))
    elif Transfer[0] == 'Tokyu':
        if Transfer[1] == 1:
            return ((1,32),(1,13),(1,6))
        elif Transfer[1] == 2:
            return ((1,28),(1,2),(1,6))
    elif Transfer[0] == ('keio', 1):
        return ((1,27),(0,0),(1,7))
    elif Transfer[0] == 'YokohamaSubway':
        return ((0,0),(5,13),(0,0))
    elif Transfer[0] == 'TamaMonorail':
        return ((18,27),(0,0),(1,7))

# 判定用関数
def judge(Set_Sta, Pass_Route, Transfer_section, Transfer, cursor):

    import Transfer_section
    import MySQLdb

    # 路線判定（支障区間と定期区間の判定）
    Route_judge = False

    # 設置駅判定（当社振替輸送対応区間と設置駅の判定）
    Sta_judge = False

    # 振替輸送情報
    ts = Transfer_conv(Transfer)

    # sqlの実行
    cursor.execute("SELECT route.Route_Abbr,Sta_number FROM `composite` JOIN route on route.id=composite.Route_id JOIN station on station.Sta_id=composite.Sta_id WHERE Route_id=1")

    # 結果の取得
    rows = cursor.fetchall()

    # 支障区間と定期区間の判定
    for passR in Pass_Route:
        for row in rows:
            if passR == row:
                Route_judge = True
                break
        if Route_judge:
            break

    # 振替輸送対応区間と設置駅の判定
    Transfer_section = Transfer_section.Transfer_segment(*ts)
    for trans_Section in Transfer_section:
        if Set_Sta == trans_Section:
            Sta_judge = True
            break

    return bool(Sta_judge and Route_judge)



def main():
    import MySQLdb
    import Transfer_section

    # 設置駅
    Set_Sta = ('OE', 9) #湘南台

    # 実施振替輸送（ex.JR1号振替→('JR', 1)）
    Transfer = ('JR', 1)

    # 定期券経路
    Pass_Route = (('JY', 4), ('JY', 17), ('OH', 28), ('OE', 13))

    # 最終判定
    Transport_judge = False



    # MySQLへ接続
    connection = MySQLdb.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        db = 'station_judge',
        charset = 'utf8'
        )

    cursor = connection.cursor()

    Transport_judge = judge(Set_Sta, Pass_Route, Transfer_section, Transfer, cursor)
    
    if Transport_judge:
        print ("通過可")
    else:
        print("通過不可")


    # 接続を閉じる
    connection.close()

if __name__ == "__main__":
    main()