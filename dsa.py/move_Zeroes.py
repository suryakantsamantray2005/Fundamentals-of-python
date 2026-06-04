class Solution:
    def movezeroes(self,nums):
        i=0
        for j in range(0,len(nums)):
           if nums[j]!=0:
               nums[i],nums[j]=nums[j],nums[i]
               i=i+1
        return nums
    
#time complexity - O(n) and space complexity - O(1)
    
obj=Solution()
print(obj.movezeroes([0,2,3,0,7,0,1]))
