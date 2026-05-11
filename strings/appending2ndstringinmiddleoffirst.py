#Append second string in the middle of first string
a=input('enter the first string ')
b=input('enter the second string ')
L=[]
for i in a:
    L.append(i)
x=(len(a)//2)
L.insert(x,b)
final=str(''.join(map(str,L)))
print(final)