#Word location in String.
s=input('enter the string ')
l=input('enter the word for location ')
count=0
found=False
a=s.split()
for i in a:
    count=count+1
    if str(i)==str(l):
      print('location of string is',count)
      found=True
      break
if not found:
        print('enter word is not present')
