#menu driven calculator , we take 2 number from the user and perform
#the calculator operations
#taking two numbers input from the user
a=int(input('enter first number '))
b=int(input('enter second number '))
#we assume the operation to be only '+','-','*','/'
op=input('enter the operation ')
if op=='+':
    print(a+b)
elif op=='-':
    print(a-b)
elif op=='*':
    print(a*b)
else:
    print (float(a/b))