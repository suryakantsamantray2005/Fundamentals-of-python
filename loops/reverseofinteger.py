#reverse of the given integer
#taking the input from the user
n=int(input('enter the integer '))
ld=0
for i in range(1,n+1):
    ld=n%10+ld
    n=n/10
print(ld)
