#taking input of 3 angles from the user and find whether it can form a triangle or not
#taking input of 3 angles from the user
a=int(input('enter the first angle(in degrees) '))
b=int(input('enter the second angle(in degrees) '))
c=int(input('enter the third angle(in degrees) '))
if a+b+c==180:
    print('it can form a triangle')
else:
    print('it can not form a triangle')