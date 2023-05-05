summ = 0
amount = 0
x = 1
while True:
    x = float(input())
    if x < 0:
        print(f"Salary can't be negative; it won't"
              f" be counted in the average")
    elif x == 0:
        break
    else:
        summ += x
        amount += 1
print(f"The average is {summ / amount}")