#Check whether the string is Symmetrical.
s=input('enter the string ')
x=int(len(s))
a=int(len(s)/2)
b=str(s[0:a])
c=str(s[a:])
if x%2==0:
 if b==c:
    print('string is symmetrical')
 else:
    print('it is unsymmetrical')
else:
  print('string is unsymmetrical')