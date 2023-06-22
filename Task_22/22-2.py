tree = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (6, 7), (7, 8)]
tree_set = set([j for i in tree for j in i])
finals = []

for i in tree_set:
    if i not in list([i[0] for i in tree]):
        finals.append(i)

pathlist = []
for i in reversed(tree):
    path = ''
    if i[1] in finals:
        path = str(i[1])
        for j in reversed(tree):
            if str(j[1]) == path[-1]:
                path += str(j[0])
    pathlist.append(path)

print(len(max(pathlist)))
