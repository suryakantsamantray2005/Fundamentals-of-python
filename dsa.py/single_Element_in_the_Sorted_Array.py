# single element in the sorted array leetcode 540
class Solution:
    def singleNonDuplicate(self,nums):
        low=1
        high=len(nums)-2
        if len(nums)==1:
            return nums[0]
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[-1]!=nums[-2]:
            return nums[-1]
        while low<=high:
            mid=(low+high)//2
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            elif (mid%2==1 and nums[mid]==nums[mid-1]) or (mid%2==0 and nums[mid]==nums[mid+1]):
                low=mid+1
            else:
                high=mid-1
# time compplexity - O(logn) and space compelexity - O(1)
obj=Solution()
print(obj.singleNonDuplicate([7,7,10,11,11,12,12]))