s1, s2 = input().split(', '), input().split(', ')

set1 = set(s1)
set2 = set(s2)

print(len(set1.intersection(set2)))
