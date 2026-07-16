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
        for i in range(1,max(nums)-min(nums)+1):
            if self.canweplacecows(nums,i,k)==True:
                ans=i
            else:
                break
        return ans
# time complexity - O(nlogn+nD) and space complexity - O(1) // D=max(nums)-min(nums)
obj=Solution()
print(obj.aggressiveCows([4, 2, 1, 3, 6],2))
