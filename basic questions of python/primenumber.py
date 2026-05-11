n=int(input('enter the integer '))
flag = True
for i in range(2,n):
    if n%i==0:
        flag = False
if flag == True:
        print('the integer is prime')
else:
        print('the integer is not prime')