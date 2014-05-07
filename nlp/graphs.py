#!/usr/bin/python3


## if len(d) == 8 ->  d[4:] = [title, text, lin, nonlin]
## if len(d) == 10 -> d[4:] = [title, text, lin, nonlin, random, common]
## if len(d) == 15 -> d[4:] = [title0%, title10%, title20%, ..., title100%]
def get_data(fname):
    lines = [line[:-1] for line in open(fname).readlines()]
    data = []
    for line in lines:
        d = []
        for item in line.split(","):
            if "." in item:
                d.append(float(item))
            elif item.isdigit():
                d.append(int(item))
            else:
                d.append(item)
        data.append(d)
    return data

#datas = []
#for fname in ["results", "results2", "results3", "results4", "results5"]:
#    datas.append(get_data(fname))
data = get_data("results")
