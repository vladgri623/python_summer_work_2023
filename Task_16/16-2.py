import re


def findall_lower(st, n):
    found = re.findall(r'\d+', st)
    lowerfound = []
    for i in found:
        if int(i) <= n:
            lowerfound.append(int(i))
    return sorted(lowerfound)


st_input = input('Input text: ')
n_input = int(input('Enter a number: '))
print(f'\n{n_input} or less than {n_input} found: ', end='')
for i in findall_lower(st_input, n_input):
    print(i, end=' ')
