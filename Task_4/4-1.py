s = input().split()
s = [float(s[0]), s[1], float(s[2])]
if s[1] == '+':
    print(s[0] + s[2])
elif s[1] == '-':
    print(s[0] - s[2])
elif s[1] == '*':
    print(s[0] * s[2])
elif s[1] == '/':
    if s[2] == 0:
        print('Cant divide by zero')
    else:
        print(s[0] / s[2])
