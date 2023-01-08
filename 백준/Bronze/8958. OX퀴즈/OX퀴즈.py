n=int(input())
arr=[]
for i in range(n):
    arr.append(input())
count=0
sums=[]
score=[]
for i in arr:
    for j in i:
        if j=="O":
            count=count+1
            sums.append(count)
        elif j =="X":
            count=0
            sums.append(count)
    score.append(sum(sums))
    count=0
    sums.clear()

for i in score:
    print(i)
