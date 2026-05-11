#if we want to read enrire lines using readline
f=open('sample1.txt','r')
while True:
    data=f.readline()
    if data=='':
        break
    else:
        print(data,end='')

f.close()