import itertools

cash = [50, 100, 200, 500, 1000, 5000]
sums = []
for j in range(2, len(cash)+1):
    for i in itertools.combinations(cash, j):
        sums.append([sum(i), i])

for i in sorted(sums):
    print(i[0], end=' = ')
    for j in range(len(i[1])-1):
        print(i[1][j], end=' + ')
    print(i[1][-1])
