#program to check the given string is palindrome or not using the slicing
s=input('enter the string ')
a=(s[::-1])
if s==a:
    print('it is palindrome')
else:
    print('it is not palindrome')