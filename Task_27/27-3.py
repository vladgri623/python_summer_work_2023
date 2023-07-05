c = 0


def count_elements(lst):
    global c
    c += len(lst)
    for i in lst:
        if type(i) == list:
            count_elements(i)


count_elements([1, 2, [3, 4, [5]]])
print(c)
