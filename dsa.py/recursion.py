class Solution:
    def recursive(self,nums,low,high,target):
        if low>high:
            return -1
        mid=(low+high)//2
        if target==nums[mid]:
            return mid
        if nums[mid]<target:
            return self.recursive(nums,mid+1,high,target)
        else:
            return self.recursive(nums,low,mid-1,target)

    def search(self,nums,target):
        low=0
        high=len(nums)-1
        return self.recursive(nums,low,high,target)
    
obj=Solution()
print(obj.search([2,3,5,6,9,10],9))
        