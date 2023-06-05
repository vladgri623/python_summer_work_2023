import re


def auto_finder(st):
    return re.findall(r"[ETOPAHKXCBM]\d\d\d[ETOPAHKXCBM][ETOPAHKXCBM]78|"
                      r"[ETOPAHKXCBM]\d\d\d[ETOPAHKXCBM][ETOPAHKXCBM]178",
                      st)


for i in auto_finder(input()):
    print(i, end=' ')
