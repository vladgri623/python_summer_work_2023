def find_noncontinuous(lst):
    lst_srt = []
    for i in range(len(lst) - 1):
        if lst[i + 1] == (lst[i] + 1):
            continue
        else:
            lst_srt.append(lst[i + 1])
    return lst_srt


n = [1, 5, 6, 7, 9, 10]

print(find_noncontinuous(n))
