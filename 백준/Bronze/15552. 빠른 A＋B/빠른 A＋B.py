import sys  # sys모듈 읽어들이기
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    a,b = map(int, input().split())
    print(a+b)