#with is use so we don't use f.close to close file it automatically closes the file
with open('sample1.txt','w') as f:
    f.write('Surya')