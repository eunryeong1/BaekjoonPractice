a=int(input())
l = list(map(int, input().split()))
number=int(input())
count=0
for i in l:
    if(i==number):
        count=count+1

print(count)