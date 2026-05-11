#we have to convert the decimal into the binary
#taking the user input
n=int(input('enter the n '))
a=n
L=[]
while n!=0:
     remainder=int(n%2)
     quotient=(n-remainder)/2
     n=quotient
     L.append(remainder)
L.reverse()
number=int(''.join(map(str,L)))
print('the binary of',a,'is',number)
print(type(number))