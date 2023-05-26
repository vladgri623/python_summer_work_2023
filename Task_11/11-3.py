roman_numbers = [(1000, 'M'), (900, 'CM'), (500, 'D'),
                 (400, 'CD'), (100, 'C'), (90, 'XC'),
                 (50, 'L'), (40, 'XL'), (10, 'X'),
                 (9, 'IX'), (5, 'V'), (4, 'IV'),
                 (1, 'I')]


def f(n):
    rn = ''
    while n > 0:
        for d, r in roman_numbers:
            while n >= d:
                rn += r
                n -= d
    return rn


x = int(input())
print(f"{x} -> {f(x)}")