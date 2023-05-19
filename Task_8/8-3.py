lst = []
print(f"Input 0 to stop")
while True:
    x = input()
    if x == '0':
        break
    else:
        lst.append(x)

ls = []
for i in lst:
    tmp = list(i)
    l = len(set(tmp))
    ls.append([l, i])
ls = sorted(ls, reverse=True)

ls_srt = []
for j in range(1, ls[0][0]+1):
    tmp2 = []
    for i in ls:
        if i[0] == j:
            tmp2.append(i)
    ls_srt.append(tmp2)

ls_srt = sorted(ls_srt, reverse=True)
for i in ls_srt:
    i.sort()
for i in ls_srt:
    for j in i:
        print(j[1], end=' ')
