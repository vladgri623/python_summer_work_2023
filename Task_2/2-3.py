import math

n = int(input("Enter a number: "))
if n < 0:
    print(f"Negative number entered")
else:
    n_fact = 1
    for i in range(1, n+1):
        n_fact *= i
    print(f"Its factorial is {n_fact}")
    print(f"math.factorial() test: {math.factorial(n)}")
