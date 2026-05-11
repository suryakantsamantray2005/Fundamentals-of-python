#a program for finding the current population if the current population is 10000
#taking the input of the year by user
cp=10000
for i in range(10,0,-1):  
    print(i ,'th year population is',cp)
    cp=cp-0.1*cp