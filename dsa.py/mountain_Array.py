# peak index in the mountain array leetcode 852
class Solution:
    def peakIndexInMountainArray(self,arr):
        if len(arr)==1:
            return arr[0]
        low=1
        high=len(arr)-2
        while low<=high:
            mid=(low+high)//2
            if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                return mid
            elif arr[mid]>arr[mid-1] and arr[mid]<arr[mid+1]:
                low=mid+1
            else:
                 high=mid-1
# time complexity - O(logn) and space complexity - O(1)
obj=Solution()
print(obj.peakIndexInMountainArray([3,9,8,6,4]))