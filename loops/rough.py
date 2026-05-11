n1=int(input('enter the number '))
n2=int(input('enter the number '))
for i in range(min(n1,n2),0,-1):
    if n1%i==0 and n2%i==0:
        print(i)

