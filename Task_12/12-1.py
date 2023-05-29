r = int(input(f"Enter the length of the list: "))
print(f"Enter numbers:")
x = [int(input()) for i in range(r)]
minx = [i for i, j in enumerate(x) if j == min(x)]
maxx = [i for i, j in enumerate(x) if j == max(x)]
print(f"\n{x}\nMin. indexes: {minx}\nMax. indexes: {maxx}")
