#Take a alphanumeric string input and print the sum and average 
#of the digits that appear in the string, ignoring all other characters.
n=input('enter the alphanumeric string ')
L=[]
for i in n:
    if i.isdigit():
        L.append(i)
if len(L)>0:
 number=int(''.join(map(str,L)))
 sum=0
 count=0
 while number>0:
    r=number%10
    sum=sum+r
    count=count+1
    number=number//10
 average=sum/count
 print('the sum is',sum)
 print('the average is',average)
else:
   print('no digits were found')