import sys

n = int(sys.stdin.readline())
l = []

for i in range(n):
    l.append(sys.stdin.readline().strip())
ls = set(l)
lst = list(ls)
lst.sort()
lst.sort(key = len)

for i in lst:
    print(i)