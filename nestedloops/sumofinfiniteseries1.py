#The natural logarithm can be approximated by the following series.
# x-1/x+(x-1/x)**2*1/2+(x-1/x)**3*1/2+....(x-1/x)**n*1/2
x=int(input('enter the x '))
n=int(input('enter the n '))
a=(x-1)/x
for i in range(2,n+1):
    result=(((x-1)/x)**i)/i
    a=a+result
print(a)