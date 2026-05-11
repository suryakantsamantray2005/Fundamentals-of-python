l1=[2,4,3]
l2=[5,6,4]
rev=0
rev1=0
l3=[]
for i in l1:
   rev=rev*10+i
for j in l2:
   rev1=rev1*10+j
while rev!=0:
   b1=rev%10
   rev=rev//10
a1=rev
while rev1!=0:
   b2=rev1%10
   rev1=rev1//10
a2=rev1
a3=a1+a2
while a3!=0:
   b3=a3%10
   a3=a3//10
   l3.append(b3)
print(l3)