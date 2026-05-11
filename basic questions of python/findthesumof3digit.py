#taking a 3 digit number input from the user
a=int(input('enter a 3 digit number'))
b=a%10
a=a//10
c=a%10
a=a//10
d=a%10
print(b+c+d)