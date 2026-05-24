class Solution:
    def missingNumber(self, nums):

        S = set(nums)

        for i in range(len(nums)+1):

            if i not in S:
                return i
            
obj=Solution()
print(obj.missingNumber([0,1,3]))