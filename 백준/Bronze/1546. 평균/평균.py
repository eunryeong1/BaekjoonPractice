N=int(input())
score=list(map(int,input().split()))
maxScore=max(score)
arr=[]
for i in score:
    arr.append(i/maxScore*100)
avg=sum(arr)/N
print(avg)
