import keyword

kwlst = keyword.kwlist
st = input()

for i in st.split():
    if i in kwlst:
        st = st.replace(i, '<kw>')
    elif i[:-1] in kwlst:
        st = st.replace(i, '<kw>')

print(st)