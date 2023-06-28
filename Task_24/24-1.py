def new_sort(lst, mm):
    if mm == 'min':
        s_lst = [lst[0]]
        for i in range(1, len(lst)):
            if lst[i] <= s_lst[-1]:
                s_lst.append(lst[i])
            else:
                for j in s_lst:
                    if lst[i] >= j:
                        s_lst.insert(s_lst.index(j), lst[i])
                        break
        return s_lst
    elif mm == 'max':
        s_lst = [lst[0]]
        for i in range(1, len(lst)):
            if lst[i] >= s_lst[-1]:
                s_lst.append(lst[i])
            else:
                for j in s_lst:
                    if lst[i] <= j:
                        s_lst.insert(s_lst.index(j), lst[i])
                        break
        return s_lst


n = [9, 3, 4, 1, 6, 8, 2, 5, 7, 0]
print(new_sort(n, 'min'))
print(new_sort(n, 'max'))
