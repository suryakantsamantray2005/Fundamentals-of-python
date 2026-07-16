# find the minimum in the rotated sorted array leetcode 153
class Solution:
    def findMin(self,nums):
        low=0
        high=len(nums)-1
        ans=float('inf')
        while low<=high:
            mid=(low+high)//2
            if nums[low]<=nums[mid]:
                ans=min(ans,nums[low])
                low=mid+1
            else:
                ans=min(ans,nums[mid])
                high=mid-1
        return ans
# tinme complexity - O(logn) and space complexity - O(1)
obj=Solution()
print(obj.findMin([4,5,6,7,0,1,2]))
