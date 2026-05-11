#Given string contains a combination of the lower and upper 
#case letters. Write a program to arrange the characters of
#a string so that all lowercase letters should come first.
a=input('enter your string ')
if type(a)==str:
 for j in a:
    if ord(j)>=97 and ord(j)<=122:
        print(str(j),end='')
 for i in a:
    if ord(i)>=65 and ord(i)<=90:
        print(str(i),end='')