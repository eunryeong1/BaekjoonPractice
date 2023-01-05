a=int(input())
org = a
i = 1
while True:
    ten=a//10
    one=a%10
    b = one*10 + (ten+one)%10

    if b == org:
        break
    else:
        a = b
        i+=1

print(i)