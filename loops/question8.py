#Print all the Armstrong numbers in a given range.
#Range will be provided by the user
#Armstrong number is a number that is equal to the sum of cubes of its digits. 
#For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.
#i only made for 3 digit number
print('ENTER RANGE')
a=int(input('From '))
b=int(input('to '))
for i in range(a,b):
    a=i
    x=a%10
    a=a//10
    y=a%10
    a=a//10
    z=a%10
    if x**3+y**3+z**3==i:
        print(i,end=',')