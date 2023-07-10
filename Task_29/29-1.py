def find_other(lst):
    if len(lst) <= 2: raise ValueError("List too small")
    n = lst[0]
    if lst.count(n) == 1:
        return n
    else:
        for i in set(lst):
            if i != n:
                return i


print(find_other([1, 2, 2, 2, 2]))
print(find_other([2, 2, 1, 2, 2]))
print(find_other([2, 2, 2, 2, 1]))
print(find_other([1, 2]))
