def frm(n):
    nl = [n for i in range(n)]
    return nl


lst = [frm(i) for i in range(1, 11)]
lst_flat = [i for j in lst for i in j]
print(lst_flat)
