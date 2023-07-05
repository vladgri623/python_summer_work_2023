def dartboard(n):
    matrix = []
    for i in range(n):
        matrix.append(list([1 for i in range(n)]))

    c = 1
    for k in range(n):
        for i in range(c, n-c):
            for j in range(c, n-c):
                matrix[i][j] = c+1
        c += 1

    for i in matrix:
        print()
        for j in i:
            print(j, end=' ')


dartboard(1)
print()
dartboard(2)
print()
dartboard(3)
print()
dartboard(5)
print()
dartboard(18)
