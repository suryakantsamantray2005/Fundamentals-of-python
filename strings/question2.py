#Removal of all characters from a string except integers
s=input('enter the alphanumeric string sentence ')
L=[]
s=s.split()
for i in s:
    if i.isdigit():
        L.append(i)
a=int(''.join(map(str,L)))
print(a)
print(type(a))