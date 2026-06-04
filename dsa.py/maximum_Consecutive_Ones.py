#maximum consecutive ones leetcode 485
class Solution:
    def findMaxConsecutiveOnes(self,nums):
        count=0
        maximum=0
        for i in range(0,len(nums)):
            if nums[i]==1:
                count=count+1
                if count>maximum:
                    maximum=count
            else:
                count=0

        return maximum
# time complexity - O(n) and space complexity - O(1)
obj=Solution()
print(obj.findMaxConsecutiveOnes([1,1,0,1,1,1]))