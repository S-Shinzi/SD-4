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
            dict.append((route_name, count))
            count += 1
    return dict


def main():
    tmp = (0, (5,13), (1,7))
    print(Transfer_segment(*tmp))


if __name__ == "__main__":
    main()