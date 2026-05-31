# right rotation of array by k elements
class Solution():
    def reverse(self,nums,left,right):
        while left<right:
          nums[left],nums[right]=nums[right],nums[left]
          left+=1
          right-=1

    def rotate(self,nums,k):
        k=k%len(nums)
        self.reverse(nums,len(nums)-k,len(nums)-1)
        self.reverse(nums,0,len(nums)-k-1)
        self.reverse(nums,0,len(nums)-1)
        return nums
# time complexity - O(n) and space complexity - O(1)
# remember the boundary of second reverse condition it is from 0 to len(nums)-k-1
    
obj=Solution()
print(obj.rotate([-1,-100,3,99],2))