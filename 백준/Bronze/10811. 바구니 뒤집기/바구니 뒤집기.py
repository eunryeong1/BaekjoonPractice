n,m=map(int,input().split())
a=[]
for i in range(1,n+1):
    a.append(i)

for i in range(0,m):
    i,j=map(int,input().split())
    b = []
    for k in range(i-1, j) :
        b.append(a[k])
    b=b[::-1]

    n = 0
    for k in range(i-1, j) :
        a[k] = b[n]
        n += 1


print(*a)