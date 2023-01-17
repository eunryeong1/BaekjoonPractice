import math
a=int(input())
for _ in range(a):
    H,W,P=map(int,(input().split()))
    YY=math.floor(P/H)+1
    XX=P%H
    if XX==0:
        YY=YY-1
        XX=H
    print(XX*100+YY)

    