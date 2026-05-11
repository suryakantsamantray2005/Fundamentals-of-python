#Display Fibonacci series up to 10 terms.
#fibonacci series starts with 1,1,2,3... 
#first we are taking user input for the numbers of terms to be displayed
n=int(input('enter the no of terms '))
firstterm=1
s=1 
for i in range(0,n):
    s=s+i