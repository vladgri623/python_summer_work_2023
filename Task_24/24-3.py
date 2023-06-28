def check_brackets(st):
    unclosed = 0
    for i in st:
        if i == '(': unclosed += 1
        elif i == ')': unclosed -= 1
    if unclosed == 0: return True
    else: return False


print(check_brackets('()'))
print(check_brackets(')(()))'))
print(check_brackets('('))
print(check_brackets('(()) (( () () ) () )'))
