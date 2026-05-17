class Solution:
    def sortedsquares(self,nums):
        L=[]
        for i in nums:
            L.append(i**2)

        L.sort()
        return L
    
obj=Solution()
print(obj.sortedsquares([-4,-1,0,3,10]))