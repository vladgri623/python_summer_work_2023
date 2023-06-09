import re

def remove_repeats(n):
    tmp = re.split(r'[\s]', n)
    for i in range(len(tmp)-1):
        if re.sub(r'\W', '', tmp[i]) == re.sub(r'\W', '', tmp[i+1]):
            tmp[i] = ''
    n_srt = ''
    for i in tmp:
        if i != '':
            n_srt = n_srt + i + ' '
    return n_srt


text = 'Напишите программу программу, которая устраняет ' \
       'повторение повторение слов, т.е. результат результат ' \
       'должен быть следующим:'
print(remove_repeats(text))

