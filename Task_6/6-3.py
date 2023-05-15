def printout(n):
    for k in n:
        print(k, end=' ')
    print()


def remove_repeats(s):
    for i in s:
        if s.count(i) > 1:
            s = s.replace(i, 'tmp', 1)
            s = s.replace(i, '')
            s = s.replace('tmp', i)
    return s


st = input()
letters, numbers, symbols = str(), str(), str()

for i in st:
    if (ord(i) > 47) and (ord(i) < 58):
        numbers += i
    elif (((ord(i) > 64) and (ord(i) < 91)) or
        ((ord(i) > 96) and (ord(i) < 123))):
        letters += i
    else:
        symbols += i


printout(remove_repeats(letters))
printout(remove_repeats(numbers))
printout(remove_repeats(symbols))
