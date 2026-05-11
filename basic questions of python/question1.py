#taking the inputs from the user of dimnsions of milk tank
#all measurements are in metre
h=float(input('enter the height of milk tank '))
l=float(input('enter the length of milk tank '))
b=float(input('enter the breadth of milk tank '))
#taking input from the user of dimensions of glass
h1=float(input('enter the height of glass '))
r=float(input('enter the radius'))
#extracting volume of milk tank
v=float(h*l*b)
#extracting volume of glass
v1=float(3.14*r*r*h1)
#finding the no of milk glass
glass=int(v/v1)
#printing the no of glass
print(glass)