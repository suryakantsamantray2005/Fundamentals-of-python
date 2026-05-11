#we have to find the factorial of a given number
#taking the input from the user
n=int(input('enter number '))
product=1
for i in range(1,n+1):
    product=product*i

print(n,'factorial is',product)