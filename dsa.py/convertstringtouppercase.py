s=input('enter the string ')
result=''
for i in s:
    if 'a'<= i <= 'z':
        result=result+chr((ord(i)-32))
    else:
        result=result+i
print(result)
print(type(result))