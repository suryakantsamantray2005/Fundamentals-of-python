#maximum product leetcode 628
class Solution(object):
    def maximumProduct(self, nums):
        nums.sort(reverse=True)
        return max(nums[0]*nums[1]*nums[2],nums[-1]*nums[-2]*nums[0])
    
#it can further optimized to O(n) time complexity and O(1) space complexity
    
obj=Solution()
print(obj.maximumProduct([-100,-98,-1,2,3,4]))