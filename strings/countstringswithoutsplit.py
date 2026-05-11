#we have to count the no of strings without using split function
#it is also the code for the split function from the scartch
s=input('enter the string ')
L=[]
temp=''
for i in s:
    if i!=' ':
        temp=temp+i
    else:
        L.append(temp)
        temp=''
L.append(temp)
print(L)