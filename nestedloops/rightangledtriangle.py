#we want to print a pattern of right angled triangle
n=int(input('enter the n '))
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end='')
    print(' ')