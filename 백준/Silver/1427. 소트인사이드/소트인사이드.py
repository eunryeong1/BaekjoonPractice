a=input()
l=[]
for i in a:
    l.append(int(i))
l.sort(reverse=True) 
for i in l:
    print(i,end='')