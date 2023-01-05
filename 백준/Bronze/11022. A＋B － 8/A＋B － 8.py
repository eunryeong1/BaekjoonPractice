import sys  # sys모듈 읽어들이기
input = sys.stdin.readline
t = int(input())
al=[]
bl=[]
for _ in range(t):
    a,b = map(int, input().split())
    al.append(a)
    bl.append(b)
for i in range(t):
    print("Case #",i+1,": ",al[i]," + ",bl[i]," = ",al[i]+bl[i],sep='')