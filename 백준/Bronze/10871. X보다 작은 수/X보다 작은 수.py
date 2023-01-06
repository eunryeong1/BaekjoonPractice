a,b=map(int,input().split())
l = list(map(int, input().split()))
result=[]
for i in l:
    if(i<b):
       result.append(i) 

print(*result)