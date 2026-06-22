# search insert position leetcode 35
class Solution:
    def searchInsert(self,nums,target):
        low=0
        high=len(nums)-1
        ans=len(nums)
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>=target:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
# time complexity - O(logn) and space complexity - O(1)
obj=Solution()
print(obj.serachInsert([1,3,5,6],2))
