# this is left rotate array of elements 
class Solution:
    def reverse(self,nums,left,right):
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
        
    def rotate(self,nums,k):
        k=k%len(nums)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,len(nums)-1)
        self.reverse(nums,0,len(nums)-1)
        return nums
# time complexity - O(n) and space complexity - O(1)

obj=Solution()
print(obj.rotate([1,2,3,4,5,6,7],3))