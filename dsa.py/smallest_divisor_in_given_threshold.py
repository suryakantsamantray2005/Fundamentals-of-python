# find the smallest divisor given a threshold leetcode 1283
class Solution:
    def smallestDivisor(self, nums, threshold):
        low=1
        high=max(nums)
        while low<=high:
            ceil=0
            mid=(low+high)//2
            for i in nums:
                j=i//mid
                if i%mid!=0:
                    j=j+1
                ceil=ceil+j
            if ceil<=threshold:
                ans=mid
                high=mid-1
            else:
                low=mid+1

        return ans
# time complexity - O(nlogm) and space complexity - O(1)
obj=Solution()
print(obj.smallestDivisor([1,2,5,9],6))