# kadane algorithm for finding the largest subarray sum
class Solution:
    def kadane(self,nums):
        current_sum=0
        maximum=float('-inf')
        for i in range(0,len(nums)):
            current_sum+=nums[i]
            if current_sum>maximum:
                maximum=current_sum
            if current_sum<0:
                current_sum=0
        return maximum
# time complexity - O(n) and space complexity - O(1)                
obj=Solution()
print(obj.kadane([-2,-3,-1,-5,-10]))