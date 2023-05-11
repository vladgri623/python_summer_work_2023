n = int(input('Enter the length of the Fibonacci sequence: '))
while n < 0:
    print('Length cannot be negative.', '\n',
          'Enter a positive number: ', sep='', end=' ')
    n = int(input())

fib0, fib1, fib2 = 1, 1, 2

if n == 0:
    print(fib0)
elif n == 1:
    print(fib0, fib1)
else:
    print(fib0, end=' ')
    for i in range(n):
        fib0 = fib1 + fib2
        fib0, fib1, fib2 = fib1, fib2, fib0
        print(fib0, end=' ')
