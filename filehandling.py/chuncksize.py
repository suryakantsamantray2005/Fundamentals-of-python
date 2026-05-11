#this will print the character in chunck size from the big file
with open('big.txt','r') as f:
    chunck_size=10
    while len(f.read(chunck_size))>0:
        print(f.read(chunck_size),end='')
        f.read(chunck_size)