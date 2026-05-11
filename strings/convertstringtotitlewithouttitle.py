#we have to convert the strings to title without using the title
s=input('enter the string ')
L=[]
for i in s.split():
    L.append(i[0].upper()+i[1:].lower())
print(" ".join(L))