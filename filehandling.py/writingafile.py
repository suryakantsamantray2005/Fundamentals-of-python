#case 1 - if the file is not present 
f=open("sample.txt",'w') #creating the file
f.write('Hello World')  #write in the file
f.close() #for closing of the file
f.write('hello') #this will not work as i close the file
