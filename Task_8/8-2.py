print(f"Entering 2-dimensional list\n"
      f"To close a list, input 'q'\n"
      f"Input 'q' again to finish input.\n")
lst = []
while True:
    minilist = []
    while True:
        x = input()
        if x == 'q':
            break
        elif x.isdigit():
            minilist.append(int(x))
    lst.append(minilist)
    if input() == 'q':
        break
    else:
        continue

# lst = [[1, 5, 3], [2, 44, 1, 4], [3, 3]]

st_list = []
for i in lst:
    i.sort(reverse=True)
    s = ''.join(map(str, i))
    st_list.append([int(s), i])
st_list.sort()

srt_list = []

for i in st_list:
    srt_list.append(i[1])
print(srt_list)
