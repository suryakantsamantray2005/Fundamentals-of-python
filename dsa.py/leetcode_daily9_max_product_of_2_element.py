# Maximum product of two element in an array leetcode 1464
class Solution:
    def maxProduct(self, nums):
        first_max=float('-inf')
        sec_max=float('-inf')
        for i in range(0,len(nums)):
            if nums[i]>first_max:
                sec_max=first_max
                first_max=nums[i]
            elif nums[i]<=first_max and nums[i]>sec_max:
                sec_max=nums[i]
        return (first_max-1)*(sec_max-1)
# time complexity - O(n) and space complexity - O(1)
obj=Solution()
print(obj.maxProduct([10,2,5,2]))