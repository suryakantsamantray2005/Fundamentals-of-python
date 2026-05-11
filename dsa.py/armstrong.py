#armstrong number
n=int(input('enter the number '))
original=n
rev=0
count=0
while n!=0:
    n=n//10
    count=count+1
length=count
n=original
while n!=0:
    rev=rev+(n%10)**length
    n=n//10
if rev==original:
    print('it is armstrong number')
else:
    print('it is not armstrong number')