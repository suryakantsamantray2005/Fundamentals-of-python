#pivot index leetcode 724
class Solution:
    def pivotIndex(self,nums):
        total_sum=sum(nums)
        left_sum=0
        for i in range(0,len(nums)):
            right_sum=total_sum-left_sum-nums[i]
            if left_sum==right_sum:
                return i
            left_sum=left_sum+nums[i]
        else:
            return -1
#time complexity - O(n) and space compelexity - O(1)
# this is the classic prefix sum question
obj=Solution()
print(obj.pivotIndex([1,7,3,6,5,6]))