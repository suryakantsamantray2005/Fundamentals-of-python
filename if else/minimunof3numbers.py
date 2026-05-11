#we have to find the minimum of 3 given numbers
#input of 3 numbers from the user
a=int(input('enter first number '))
b=int(input('enter second number '))
c=int(input('enter third number '))
#using if else we have to compare the 3 numbers
if a<b and a<c:
    print('first number is minimum')
elif b<a and b<c:
    print('second number is minimum')
else:
    print('third number is minimum')