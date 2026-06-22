# remove duplicates 2 leetcode 80
class Solution:
    def removeDuplicates(self,nums):
        if len(nums)<=2:
            return len(nums)
        write=2
        for i in range(2,len(nums)):
            if nums[write-2]!=nums[i]:
                nums[write]=nums[i]
                write+=1
        return write
# time complexity - O(n) and space complexity - O(1)
obj=Solution()
print(obj.removeDuplicates([0,0,1,1,1,1,2,3,3]))