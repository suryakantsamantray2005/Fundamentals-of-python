#we have to find the sum of a series by providing the user input of n
# 1+x^2/2+x^3/3+....x^n/n
#n and  will be provided by the user
n=int(input('enter the n '))
x=int(input('enter the x '))
result=1
for i in range(2,n+1):
    sum=(x**i)/i
    result=result+sum
print(result)