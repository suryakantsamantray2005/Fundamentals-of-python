#contains duplicate leetcode 217
class Solution:
    def containsDuplicate(self,nums):
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                return True
        return False
obj=Solution()
print(obj.containsDuplicate([1,2,3,4]))
