import re


def phone_finder(st):
    return re.findall(r"\+7\(812\)\d\d\d-\d\d\d\d|"
                      r"\+7\(812\)\d\d\d-\d\d-\d\d|"
                      r"\+7\(921\)\d\d\d-\d\d\d\d|"
                      r"\+7\(921\)\d\d\d-\d\d-\d\d",
                      st)


for i in phone_finder(input()):
    print(i, end=' ')
