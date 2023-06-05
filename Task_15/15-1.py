lst = list()


def dct_key_sorter(dct, key):
    for i in dct.values():
        if type(i) == int:
            if dct.get(key) == i:
                lst.append(i)
        elif type(i) == dict:
            dct_key_sorter(i, key)


d = {1:1, 2:2, 3:{2:22, 3:{1:111, 2:222, 3:{0:1111, 1:2222, 2:3333}}, 1:11}, 6:22}
dct_key_sorter(d, int(input()))
print(lst)
