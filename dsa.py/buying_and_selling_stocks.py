# buying and selling stocks leetcode 121
class Solution:
    def maxProfit(self,nums):
        i=0
        j=1
        max_profit=0
        while i<len(nums) and j<len(nums):
            if nums[i]>nums[j]:
                i=j
                j=j+1
            else:
                profit=nums[j]-nums[i]
                if profit>max_profit:
                    max_profit=profit
                j=j+1
        return max_profit
# time complexity - O(n) and space complexity -O(1)
obj=Solution()
print(obj.maxProfit([2,1,2,1,0,1,2]))