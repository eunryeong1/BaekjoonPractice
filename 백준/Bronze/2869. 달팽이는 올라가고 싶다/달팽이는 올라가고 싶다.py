A, B, V = map(int, input().split())
k=(V-A)%(A-B)
if k==0:
    print(int((V-A)//(A-B))+1)
else :
    print(int((V-A)//(A-B))+2)