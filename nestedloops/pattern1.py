#we have to print the following pattern
#1
#1 2 1
#1 2 3 2 1
#1 2 3 4 3 2 1 if we enter the input 4
n=int(input('enter the n '))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end='')
    for k in range(i-1,0,-1):
        print(k,end='')
    print('')