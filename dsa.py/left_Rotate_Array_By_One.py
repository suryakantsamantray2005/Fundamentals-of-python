#left rotate of array by one 
class Solution:
    def rotate(self,nums):
        temp=nums[0]
        for i in range(1,len(nums)):
            nums[i-1]=nums[i]
        nums[-1]=temp
        return nums
obj=Solution()
print(obj.rotate([1,2,3,4,5]))