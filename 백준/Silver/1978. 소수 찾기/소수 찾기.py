n=int(input()) 
num_list = list(map(int, input().split(' ')))
Cnt=0
for i in num_list:
    cnt=0
    if i==1:
        continue
    
    for j in range(2, i+1):
        if((i%j)==0):
            cnt += 1
    if(cnt == 1):
        Cnt += 1
print(Cnt)
