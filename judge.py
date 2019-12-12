# mysqlclient-1.4.5



# 入力された振替情報から振替区間に相当する駅のSELECT文を作成
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

    tmp = eval(Transfer[0])[Transfer[1]]

    if (type(tmp) is int):
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
def GetTable(sql):
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
    cursor.execute(sql)

    # 結果の取得
    rows = cursor.fetchall()

    # 接続を閉じる
    connection.close()

    return rows


# 路線判定（支障区間と定期区間の判定） 
def RouteJudge(Pass_Route, Transfer):

    sql = CreateSQL(Transfer)

    rows = GetTable(sql)

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

# 駅判定（振替輸送対応区間と設置駅の判定）
def StationJudge(Transfer, Set_Sta):
    import Transfer_section

    # 設置駅判定
    Sta_judge = False

    ts = Transfer_section.Transfer_conv(Transfer)

    Sta_list = Transfer_section.Transfer_segment(*ts)
    for trans_Section in Sta_list:
        if Set_Sta == trans_Section:
            Sta_judge = True
            break

    return Sta_judge


# 最終判定
def Transport_judge(Route_judge, Sta_judge):

    Transport_judge = False
    
    Transport_judge = Route_judge and Sta_judge

    if Transport_judge:
        print ("通過可")
    else:
        print("通過不可")



def main():

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
    Transfer = ('YokohamaSubway', 1)

    # 定期券経路
    Pass_Route = (('JY', 4), ('JY', 17), ('OH', 28), ('OE', 13))


    Route_judge = RouteJudge(Pass_Route, rows)

    Sta_judge = StationJudge(Transfer, Set_Sta)

    Transport_judge(Route_judge, Sta_judge)


if __name__ == "__main__":
    main()