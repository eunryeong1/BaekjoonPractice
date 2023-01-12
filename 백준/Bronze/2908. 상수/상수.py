a,b=((input().split()))
reverse=''
num1=a[::-1]
num2=b[::-1]

if(int(num1)>int(num2)):
    print(num1)
elif(int(num1)<int(num2)):
    print(num2)