a=int(input("enter the integer "))
digits='0123456789'
s=''
for i in str(a):
    s=s+str(digits.index(i))
print(s)
print(type(s))