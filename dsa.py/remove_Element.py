# leetcode 27
class Solution:
    def removeElement(self,nums,val):
        j=0
        for i in range(0,len(nums)):
            if nums[i]!=val:
                nums[i],nums[j]=nums[j],nums[i]
                j=j+1
        return j
    
# time complexity - O(n) and space complexity - O(1)
obj=Solution()
print(obj.removeElement([3,2,2,3],3))