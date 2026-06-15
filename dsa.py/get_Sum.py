class Solution:
    def getSum(self,a,b):
        count=0
        if a>0:
            for i in range(0,a):
                count+=1
        if b>0:
            for i in range(0,b):
                count+=1
        if a<0:
            for i in range(0,abs(a)):
                count-=1
        if b<0:
            for i in range(0,abs(b)):
                count-=1
        return count