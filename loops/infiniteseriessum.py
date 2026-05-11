#we have to find the series sum of 1/1!+2/2!+3/3!......nth term
#find the sum of the series 
##taking input from the user 
n=int(input('enter the nth term ')) 
product=1 
totalsum=0 
for i in range(1,n+1): 
    product=product*i 
    totalsum=totalsum+(i/product) 
print(totalsum) 