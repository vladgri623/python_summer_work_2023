import re


def abbreviate(st):
    abbr_st = ''
    ltr = re.findall(r'\b\w', st)
    for i in ltr:
        abbr_st += i.upper()
    return abbr_st


print(abbreviate(input()))
