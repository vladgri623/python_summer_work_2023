def interval_list(x):
    # turning the string into a list of intervals
    x = x.split(',')
    x_i = [[int(j) for j in i.split('-')] for i in x]
    # generates the final list
    x_final = []
    for i in x_i:
        for j in range(i[0], i[1]+1):
            x_final.append(j)
    return x_final


print(interval_list(input()))
