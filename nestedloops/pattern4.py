#we want to print the pyramid
#     *
#    * * *
#    * * * * *
n=int(input('enter the n '))
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(' ',end='')
    for k in range(1,2*i):
     print('*',end='')
    print()