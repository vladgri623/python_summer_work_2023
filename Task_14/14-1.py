def digitcount(n):
    if n < 10:
        return 1
    else:
        return 1 + digitcount(n // 10)


x = int(input('Enter a number: '))
print(f"This number has {digitcount(x)} digits.")
