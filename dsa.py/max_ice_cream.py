class Solution:
    def maxIceCream(self,costs,coins):
        costs.sort()
        total=0
        count=0
        for i in range(0,len(costs)):
            total=total+costs[i]
            if total<=coins:
                count+=1
            else:
                total=total-costs[i]
        return count
obj=Solution()
print(obj.maxIceCream([1,3,2,4,1],7))