import sys  # sys모듈 읽어들이기
input = sys.stdin.readline
t = int(input())
l=[]
for _ in range(t):
    a,b = map(int, input().split())
    l.append(a+b)
for i in range(t):
    print("Case #",i+1,": ",l[i],sep='')