def tri_2(n):
    if n == 1:
        print('*')
    else:
        print('*'*n)
        tri_2(n-1)
        print('*'*n)


x = int(input("Enter the size of the triangles: "))
tri_2(x)
