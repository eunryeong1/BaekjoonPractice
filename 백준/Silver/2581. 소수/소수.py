a=int(input()) 
b=int(input())
sosu=[]
for i in range(a,b+1):
    cnt=0
    if i==1:
        continue
    
    for j in range(2, i+1):
        if((i%j)==0):
            cnt += 1
    if(cnt == 1):
        sosu.append(i)
if(len(sosu)==0):
    print("-1")
else:
    print(sum(sosu))
    print(min(sosu))

