# split array largest sum leetcode 410
class Solution:
    def splitArray(self, nums, k):
        ans=-1
        low=max(nums)
        high=sum(nums)
        while low<=high:
            total_sum=0
            total_subarrays=1
            mid=(low+high)//2
            for i in nums:
                total_sum+=i
                if total_sum>mid:
                    total_sum=i
                    total_subarrays+=1
            if total_subarrays>k:
                low=mid+1
            else:
                high=mid-1
                ans=mid

        return ans
# time complexity - O(nlogn) and space complexity - O(1)
obj=Solution()
print(obj.splitArray([1,4,4],3))