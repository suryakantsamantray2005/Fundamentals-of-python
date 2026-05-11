#we have to find the LCM of two numbers
n1=int(input('enter the first number '))
n2=int(input('enter the second number '))
i=1
j=1
A=[]
B=[]
while i>0:
    product=i*n1
    i=i+1
    A.append(product)
while j>0:
    product1=j*n2
    j=j+1
    B.append(product1)
if product==product1:
    print(min(product))