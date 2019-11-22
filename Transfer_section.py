# 振替情報を与えるとそれに対応した小田急の振替対応範囲の駅一覧をリストで出力する


# 振替輸送に対応する当社振替輸送区間を小田原線、江ノ島線、多摩線ごとに駅ナンバーで出力
def Transfer_conv(Transfer):
    if Transfer == ('JR', 10):
        return ((1,18),(0,0),(0,0))
    elif Transfer[0] == 'JR' or 'Sotetu' or 'Toei':
        return ((1,47),(1,16),(1,7))
    elif Transfer[0] == 'ToykoMetro':
        return ((1,7),(0,0),(0,0))
    elif Transfer[0] == 'Tokyu':
        if Transfer[1] == 1:
            return ((1,32),(1,13),(1,6))
        elif Transfer[1] == 2:
            return ((1,28),(1,2),(1,6))
    elif Transfer[0] == ('Keio', 1):
        return ((1,27),(0,0),(1,7))
    elif Transfer[0] == 'YokohamaSubway':
        return ((0,0),(5,13),(0,0))
    elif Transfer[0] == 'TamaMonorail':
        return ((18,27),(0,0),(1,7))

# (小田原線, 江ノ島線, 多摩線)となっている駅ナンバーからすべての駅を１つのリストにして出力
def Transfer_segment(oh, oe ,ot):
    count = 1
    dict = []
    Sta_count = 0
    for i in range(4):
        count = 1
        if i == 1:
            count = oh[0]
            Sta_count = oh[1]
            route_name = 'OH'
        elif i == 2:
            count = oe[0]
            Sta_count = oe[1]
            route_name = 'OE'
        elif i == 3:
            count = ot[0]
            Sta_count = ot[1]
            route_name = 'OT'
        
        while (count <= Sta_count):
            if count == 0:
                break
            dict.append((route_name, count))
            count += 1
    return dict


def main(Railway, Nomber):
    transfer = (Railway, Nomber)
    tmp = Transfer_conv(transfer)
    print(Transfer_segment(*tmp))


if __name__ == "__main__":
    main('JR', 10)