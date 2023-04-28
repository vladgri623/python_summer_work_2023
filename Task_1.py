import math

# # 1-1
# x, y = int(input()), int(input())
# print(x + y, x * y)

# 1-2 1-3
x, y = float(input()), float(input())
summ, diff, mult, div, ddiv = (x + y), (x - y), (x * y), (x / y), (x // y)
largest, second = -math.inf, -math.inf


if summ > largest:
    largest = summ
if (summ < largest) and (summ > second):
    second = summ

if diff > largest:
    largest = diff
if (diff < largest) and (diff > second):
    second = diff

if mult > largest:
    largest = mult
if (mult < largest) and (mult > second):
    second = mult

if div > largest:
    largest = div
if (div < largest) and (div > second):
    second = div

if ddiv > largest:
    largest = ddiv
if (ddiv < largest) and (ddiv > second):
    second = ddiv


print(summ, diff, mult, div, ddiv, '\n', largest, second)