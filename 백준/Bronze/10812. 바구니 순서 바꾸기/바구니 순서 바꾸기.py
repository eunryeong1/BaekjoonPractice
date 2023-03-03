n,m=map(int,input().split())
a=[]
for i in range(1,n+1):
    a.append(i)
for i in range(0,m):
    b,e,m=map(int,input().split())
    a = a[:b-1] + a[m-1:e] + a[b-1:m-1] + a[e:]

print(*a)