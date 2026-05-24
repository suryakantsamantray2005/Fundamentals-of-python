#missing number leetcode 268
class Solution:
    def missingNumber(self,nums):
        n=len(nums)+1
        actual=(n*(n-1))/2
        original=sum(nums)
        return int(actual-original)

obj=Solution()
print(obj.missingNumber([3,0,1]))