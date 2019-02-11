a=[1,2,3,4,5,6,7,8,9]
n=3
b=[]
for j in range(n):
    for i in range(0,n*n,n):
        b.append(a[i+j])
    b=b[::-1]
    for i in b:
        print(i,end=" ")
    b=[]

