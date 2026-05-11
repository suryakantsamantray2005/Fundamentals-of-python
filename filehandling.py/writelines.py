#i want to add lines from the list 
L=['hello\n','hi\n','how are you\n','I am fine']
f=open('sample1.txt','w')
f.writelines(L)
f.close()