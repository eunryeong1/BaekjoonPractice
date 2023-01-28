import statistics
from collections import Counter
import sys
n=int(sys.stdin.readline())
a=[]
for i in range(n):
    a.append(int(sys.stdin.readline()))

a=sorted(a)

print(round(sum(a)/len(a)))
print(statistics.median(a))
cnt = Counter(a).most_common(2)

if len(a) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
print(max(a)-min(a))