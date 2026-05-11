#login program identification 
#we have assume email-> surya@gmail.com and password-> 1234 
#taking the input of emial and password from the user
a=input('enter the email ')
b=input('enter password ')
#using if else statement
if a==('surya@gmail.com') and b==('1234'):
    print('WELCOME USER')
elif a==('surya@gmail.com') and b!=('1234'):
    print('password is incorrect')
elif a!=('surya@gmail.com') and b==('1234'):
    print('email is incorrect') 
else:
    print('email id and password is incorrect')

