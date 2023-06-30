def camelcase(st):
    cc_st = ''
    for i in st.split():
        tmp = i[0].upper() + i[1:].lower()
        cc_st += tmp
    return cc_st


print(camelcase('CAMEL Case wORD'))
