import math

lst = []
lst_len = int(input('List length: '))
for i in range(lst_len):
    lst.append(int(input()))

for i in range(len(lst)):
    m = math.inf
    if m > lst[i]:
        m = lst[i]
print(f"Smallest number: {m}")
