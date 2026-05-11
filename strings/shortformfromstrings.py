#we want to convert short forms using initial strings
a=input('enter the string ')
a=a.title()
for i in a:
    if ord(i)>=65 and ord(i)<=90:
        print(str(i),end='')

print()

#another way of doing
a=input('enter the string ')
words=a.split()
for i in words:
    print(i[0].upper(),end='')