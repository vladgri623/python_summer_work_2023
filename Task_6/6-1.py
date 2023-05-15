roman_numbers = [(1000, 'M'), (900, 'CM'), (500, 'D'),
                 (400, 'CD'), (100, 'C'), (90, 'XC'),
                 (50, 'L'), (40, 'XL'), (10, 'X'),
                 (9, 'IX'), (5, 'V'), (4, 'IV'),
                 (1, 'I')]


def roman_to_decimal(roman):
    decimal = 0
    for i, j in roman_numbers:
        while roman.startswith(j):
            decimal += i
            roman = roman[len(j):]
    return decimal


x = ''
print('Enter a roman number to convert into a decimal', '\n',
      'Enter 0 to stop', sep='')
while x != '0':
    x = input()
    print(roman_to_decimal(x))
