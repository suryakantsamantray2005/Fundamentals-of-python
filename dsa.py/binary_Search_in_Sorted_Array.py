# binary search in sorted array
class Solution:
    def search(self,nums,target):
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            if target>nums[mid]:
                low=mid+1
            if target<nums[mid]:
                high=mid-1
        return -1
# time complexity - O(logn) and space complexity - O(1)

obj=Solution()
print(obj.search([-1,0,3,5,9,12],2))