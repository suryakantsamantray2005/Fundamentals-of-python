#maximum product difference between two pairs
#Input: nums = [5,6,2,7,4]
#Output: 34
#Explanation: We can choose indices 1 and 3 for the first pair (6, 7) and 
#indices 2 and 4 for the second pair (2, 4).
#The product difference is (6 * 7) - (2 * 4) = 34.
class Solution:
    def maxProductDifference(self,nums):
        nums.sort()
        product=nums[-1]*nums[-2] - nums[0]*nums[1]

        return product
    
#this has time complexity of O(N logN)

obj=Solution()
print(obj.maxProductDifference([-10,-9,1,2]))