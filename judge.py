# mysqlclient-1.4.5


# 路線判定（支障区間と定期区間の判定） 
def judge_1(Pass_Route, rows):

    # 路線判定（支障区間と定期区間の判定）
    Route_judge = False

    # 支障区間と定期区間の判定
    for passR in Pass_Route:
        for row in rows:
            if passR == row:
                Route_judge = True
                break
        if Route_judge:
            break
    
    return Route_judge

# 振替輸送対応区間と設置駅の判定
def judge_2(Transfer, Set_Sta):
    import Transfer_section

    # 設置駅判定
    Sta_judge = False

    ts = Transfer_section.Transfer_conv(Transfer)

    Transfer_section = Transfer_section.Transfer_segment(*ts)
    for trans_Section in Transfer_section:
        if Set_Sta == trans_Section:
            Sta_judge = True
            break

    return Sta_judge

# create sql
def CreateSQL(Transfer):

    sql = "SELECT route.Route_Abbr,Sta_number FROM `composite` JOIN route on route.id=composite.Route_id JOIN station on station.Sta_id=composite.Sta_id WHERE "

    JR = {1:1, 2:2, 3:(2,3), 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10}
    Toei = {1:11, 2:11, 3:11, 4:12, 5:12, 6:13, 7:14}
    TokyoMetro = {1:15, 2:(16,17), 5:18, 9:19, 20:(15,16,17,18,19,20,21,22,23,24)}
    Tokyu = {1:(25,26,27,28,29,30),2:31}
    Keio = {1:(37,32)}
    Sotetu = {1:33}
    YokohamaSubway = {1:(34,35)}
    TamaMonorail = {1:36}

    if (type(eval(Transfer[0])[Transfer[1]]) is str):
        sql += 'Route_id='+str((eval(Transfer[0])[Transfer[1]]))
    else:
        tmp = eval(Transfer[0])[Transfer[1]]
        isFirst = True
        for i in tmp:
            if isFirst:
                sql += 'Route_id='+str(i)
                isFirst = False
                continue
            sql += ' or Route_id='+str(i)


    sql += ';'

    return sql




# DBに接続し、sqlを実行、結果をreturnする
def SQL(sql):
    import MySQLdb

    # MySQLへ接続
    connection = MySQLdb.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        db = 'station_judge',
        charset = 'utf8'
        )

    cursor = connection.cursor()

    # sqlの実行
    cursor.execute("SELECT route.Route_Abbr,Sta_number FROM `composite` JOIN route on route.id=composite.Route_id JOIN station on station.Sta_id=composite.Sta_id WHERE Route_id=1")

    # 結果の取得
    rows = cursor.fetchall()

    # 接続を閉じる
    connection.close()

    return rows


def main():
    import Transfer_section

    # 設置駅
    Set_Sta = ('OE', 9) #湘南台

    # 実施振替輸送（ex.JR1号振替→('JR', 1)）
    Transfer = ('JR', 1)

    # 定期券経路
    Pass_Route = (('JY', 4), ('JY', 17), ('OH', 28), ('OE', 13))

    # 最終判定
    Transport_judge = False
    
    if Transport_judge:
        print ("通過可")
    else:
        print("通過不可")


if __name__ == "__main__":
    main()