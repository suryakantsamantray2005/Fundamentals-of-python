#third max leetcode
class Solution:
    def thirdMax(self,nums):
        L=list(set(nums))
        L.sort(reverse=True)
        if len(L)>=3:
            return L[2]
        else:
            return max(L)
        
#this solution further can be optimized to O(n) try this S
    
obj=Solution()
print(obj.thirdMax([3,1,2,2]))