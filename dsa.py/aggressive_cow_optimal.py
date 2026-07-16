class Solution:
    def canweplacecows(self, nums, dist,k):
        countcows=1
        lastcows=nums[0]
        for i in range(1,len(nums)):
            if nums[i]-lastcows>=dist:
                countcows+=1
                lastcows=nums[i]
        if countcows>=k:
            return True
        else:
            return False
    def aggressiveCows(self, nums, k):
        nums.sort()
        low=1
        high=nums[-1]-nums[0]
        while low<=high:
            mid=(low+high)//2
            if self.canweplacecows(nums,mid,k)==True:
                low=mid+1
            else:
                high=mid-1
        return high
# time complexity - O(nlogn+nlogD) aand space complexity - O(1) // D=nums[-1]-nums[0]
obj=Solution()
print(obj.aggressiveCows([1,2,3,4,5],2))