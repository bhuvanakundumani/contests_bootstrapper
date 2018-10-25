def print_pascalstriangle(a):
    
    n = len(a)
    # printing pascal's triangle
    print()
    print( "Your Pascal's triangle for the number {}".format(n))
    print()
    for i in range(n):
        print("   "*(n-i),end=" ",sep=" ")
        for j in range(0,i+1):
            print('{0:6}'.format(a[i][j]),end=" ",sep=" ")
        print()





def pascals_triangle(n):
    a=[]
    for i in range(n):
        a.append([])
        a[i].append(1)
        for j in range(1,i):
            a[i].append(a[i-1][j-1]+a[i-1][j])
        if(n!=0):
            a[i].append(1)
    return a




print("Welcome to Pascal's triangle:")


n=int(input("Enter number of rows for the pascal's triangle: "))
b=[]
# pascal's triangle is generated
b = pascals_triangle(n)
# pascal's triangle gets printed here
print_pascalstriangle(b)
