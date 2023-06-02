def digit_sum(n):
    if n < 10:
        return n
    else:
        return (n % 10) + digit_sum(n // 10)


x = int(input('Enter a number: '))
print(f"The sum of its digits is {digit_sum(x)}")
