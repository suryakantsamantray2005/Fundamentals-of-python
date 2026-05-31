# right rotate of array by k leetcode 189
class Solution:
    def rotateArrayByOne(self,nums):
        k=len(nums)-1
        for i in range(0,len(nums)):
            nums[i],nums[k]=nums[k],nums[i]
    def rotate(self,nums,k):
        for j in range(0,k):
            self.rotateArrayByOne(nums)

        return nums
# this solution is right but its time complexity will become O(nk) which is not optimal
#optimal solution O(n) and space complexity O(1)
    
obj=Solution()
print(obj.rotate([1,2,3,4,5,6,7],8))