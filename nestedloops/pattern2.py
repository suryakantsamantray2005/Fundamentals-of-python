#we want to print pattern
#5 4 3 2 1
#4 3 2 1
#3 2 1
#2 1
#1
n=int(input('enter the n '))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end='')
    print()