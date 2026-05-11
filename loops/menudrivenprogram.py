#its a menu driven program
#1.cm to ft ,2.km to miles ,3.USD to INR, 4.exit
print("WELCOME USER!!!")
print("1.cm to ft")
print("2.km to miles")
print("3.USD to INR")
print("4.exit")
a=int(input('enter '))
if a==1:
    b=float(input('enter cm '))
    b=float(b/30.48)
    print('foot is',b)
elif a==2:
    c=float(input('enter km '))
    c=float(c/1.609)
    print('miles is',c)
elif a==3:
    d=float(input('enter USD '))
    d=float(d*90)
    print('INR is',d)
else:
    print('exit')