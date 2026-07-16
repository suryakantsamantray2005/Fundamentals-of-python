# find the Kth Missing positive number leetcode 1539
class Solution:
    def findKthPositive(self, arr, k):
        low=0
        high=len(arr)-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]-(mid+1)<k:
                low=mid+1
            else:
                high=mid-1
        return low+k
# this can be solve in O(n) time complexity but the most optimal is O(logn) and space 
# cpomplexity will be O(1)
obj=Solution()
print(obj.findKthPositive([1,2,3,4],2))