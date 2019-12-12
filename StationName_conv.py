# OCRから受け取ったリストを駅ナンバリングに変換

class station():
    def __init__(self,ocrList):
        self.Entry_route = []
        self.set_Route(ocrList)
    
    def set_Route(self, ocrList):
        self.Entry_route = ocrList

    def get_Route(self):
        return self.Entry_route

def CreatePassRoute(ocrList):

    import re

    pattern_Route = re.compile(r'線$')

    # リストの並び替え
    tmp = [ocrList[0]]

    for i in ocrList[2].split("・"):
        if bool(re.search(pattern_Route, i)):
            continue
        tmp.append(i)
    
    tmp.append(ocrList[1])

    #ocrListは[発駅, 乗換駅1 ,(乗換駅2), ... ,着駅]のようになる。 ()はオプション
    ocrList = tmp

    sql = ""
    pass_route = []
    station_list = []

    for name in ocrList:
        sql = CreateSQL(name)
        rows = GetTable(sql)
        station_list.append(station(rows))
    
    count = 0
    
    for i in station_list:
        if count == 0:
            Sta_tmp1 = i.get_Route()
            count += 1
            continue
        
        Sta_tmp = i.get_Route()

        for j in Sta_tmp1:
            for k in Sta_tmp:
                if((j[0] == k[0])or((j[0]=='OH' or j[0]=='OE' or j[0]=='OT')and(k[0]=='OH' or k[0]=='OE' or k[0]=='OT'))):
                    pass_route.append(j)
                    pass_route.append(k)
                    continue

        Sta_tmp1 = Sta_tmp
        count += 1
            
        
    return pass_route



def CreateSQL(sta_name):

    sql = "SELECT route.Route_Abbr,Sta_number,station.Sta_Name FROM `composite` JOIN route on route.id=composite.Route_id JOIN station on station.Sta_id=composite.Sta_id WHERE "

    sql += "Sta_Name LIKE \"%"+sta_name

    sql += "%\";"

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


def main():
    pri = CreatePassRoute(['長後', 'あざみ野', '中央林間・田園都市線'])
    print(pri)

if __name__ == '__main__':
    main()