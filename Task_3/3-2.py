number = int(input())
number_list = []
for i in range(10):
    number_list.append(str(number).count(str(i)))
    print(f"{i} - {number_list[i]}")