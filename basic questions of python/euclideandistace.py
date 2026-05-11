#taking user input of coordinates
a=int (input ('enter x1 coordinate '))
b=int (input('enter y1 coordinate '))
c=int (input('enter x2 coordinate '))
d=int (input ('enter y2 coordinate '))
#applying formula (arithmetic operator is used)
r=float((c-a)*(c-a)+(d-b)*(d-b))**0.5
print(r)