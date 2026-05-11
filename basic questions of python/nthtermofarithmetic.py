#taking the input of first and second term from the user
a=int(input('enter the first term '))
b=int(input('enter the second term '))
#taking input of nth term
c=int(input('enter the nth term '))
#taking the common difference d
d=int(b-a)
#applying the formula let the nth term be denoted as Tn
Tn=int(a+c*d-d)
#print the result
print(Tn)