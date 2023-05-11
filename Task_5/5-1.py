n = int(input('Enter the size of the Pascal triangle: '))
while n <= 0:
    print('Cannot generate Pascals triangle for this number', '\n',
          'Enter a positive number: ', sep='', end=' ')
    n = int(input())

triangle = dict()
triangle[0] = [1]
triangle[1] = [1, 1]

if n == 1:
    print(1)
elif n == 2:
    print(1)
    print(1, ' ', 1, sep='')
else:
    for j in range(2, n):
        tmp = list()
        tmp.append(1)
        for i in range(len(triangle[j-1])-1):
            tmp.append(triangle[j-1][i] + triangle[j-1][i+1])
        tmp.append(1)
        triangle[j] = tmp

    for i in range(len(triangle)):
        for j in triangle[i]:
            print(j, end=' ')
        print('\n', end='')
