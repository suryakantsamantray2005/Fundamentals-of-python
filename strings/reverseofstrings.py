#We are given a string and we need to reverse 
#words of a given string.
#ex.  geeks quiz practice code
#output code practice quiz geeks
s=input('enter the string ')
a=s.split()
for j in a[-1::-1]:
    print(j,end=' ')