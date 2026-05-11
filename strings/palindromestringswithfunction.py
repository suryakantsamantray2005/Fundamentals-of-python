#we have to check the palindrome of the strings without using the slicing
s=input('enter the string ')
flag=True
for i in range(0,len(s)//2): 
    if s[i]!=s[len(s)-i-1]:
        flag=False
        print('not a palindrome')
if flag:
    print('it is palindrome')  