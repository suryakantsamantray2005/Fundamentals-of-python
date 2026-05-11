#Find uncommon words from two Strings.
A=input('enter the first string ')
B=input('enter the second string ')
a=A.split()
b=B.split()
s1=set(a)
s2=set(b)
s3=s1^s2
uncommonelement=list(s3)
print(uncommonelement)
print(type(uncommonelement))