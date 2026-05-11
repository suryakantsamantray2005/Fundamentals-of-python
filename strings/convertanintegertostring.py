#we have to convert the integer into string
#eg. int(2)>----output: '2'
number=int(input('ente the number '))

digits='0123456789'
result=''
while number!=0:
    result=digits[number%10]+result
    number=number//10
print(result)
print(type(result))