#checking if the number is palindrome or not 
n=int(input('enter the number '))
original=n
rev=0
while n!=0:
    a=n%10
    rev=rev*10+a
    n=n//10
if rev==original:
    print('it is palindrome')
else:
    print('not palindrome')