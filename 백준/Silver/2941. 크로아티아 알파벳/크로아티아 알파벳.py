c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
a = input()

for i in c :
    a = a.replace(i, '*')  # input 변수와 동일한 이름의 변수
print(len(a))