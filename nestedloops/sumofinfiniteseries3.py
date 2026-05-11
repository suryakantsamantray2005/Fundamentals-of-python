#Write a program to calculate the sum of series up to n term. 
# For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690. 
# Take the user input and then calculate. And the output style should match which is given in the example
n=int(input('enter the n '))
a=2
total=2
print(a,end='')
for i in range(1,n):
    a=a*10+2
    total=total+a
    print('+',a,end='')
print('=',total)