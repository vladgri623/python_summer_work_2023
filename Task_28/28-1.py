def find_inversions(lst):
    inv = 0
    for i in range(len(lst)):
        tmp = lst[i:]
        for j in range(len(tmp)):
            if tmp[j] < lst[i]:
                inv += 1
    return inv


print(find_inversions([1, 2, 3, 4, 5]))
print(find_inversions([5, 4, 3, 2, 1]))
