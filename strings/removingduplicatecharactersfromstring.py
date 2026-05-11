#Write a program that can remove all the duplicate 
#characters from a string. User will provide the input.
s=input('enter the string ')
result=''
for i in s:
    if i not in result:
     result=result+i
print(result)