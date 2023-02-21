n,m=map(int,input().split())
a=[]
for i in range(1,n+1):
    a.append(i)

for i in range(0,m):
    i,j=map(int,input().split())
    a[i-1],a[j-1]=a[j-1],a[i-1]
    

print(*a)