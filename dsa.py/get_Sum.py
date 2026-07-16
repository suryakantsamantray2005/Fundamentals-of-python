# get sum leetcode 371
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
    
# this is not the optimized code as it can be done with bit manupalation(XOR)