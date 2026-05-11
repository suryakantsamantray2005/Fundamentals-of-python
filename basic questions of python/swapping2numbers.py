#taking input from the user 
fnum=int (input ('enter first number '))
snum =int (input('enter the second number '))
#creating a variable
temp =int (fnum)
fnum=int (snum)
snum =int (temp)
#print the result after creating the variable and code
print('after swapping:',fnum,snum)