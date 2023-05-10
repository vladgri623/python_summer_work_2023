sent1 = input().lower()
sent2 = input().lower()

for i in sent1:
    if (ord(i) > 96) and (ord(i) < 123):
        continue
    else:
        sent1 = sent1.replace(i, '')

for i in sent2:
    if (ord(i) > 96) and (ord(i) < 123):
        continue
    else:
        sent2 = sent2.replace(i, '')

dct1 = dict()
dct2 = dict()

for i in sent1:
    if i in dct1:
        dct1[i] += 1
    else:
        dct1[i] = 1
for i in sent2:
    if i in dct2:
        dct2[i] += 1
    else:
        dct2[i] = 1

if dct1 == dct2:
    print(True)
else:
    print(False)
