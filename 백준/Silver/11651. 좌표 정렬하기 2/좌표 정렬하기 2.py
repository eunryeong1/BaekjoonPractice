N=int(input())
arr=[]
for i in range(N):
    a,b = map(int,input().split())
    arr.append((b,a))
arr.sort()
for b,a in arr:
    print(a,b)