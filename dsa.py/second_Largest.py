class Solution:
    def secondLargest(self,nums):
        maximum=nums[0]
        second_largest=float('-inf')
        for i in range(0,len(nums)):
            if nums[i]>maximum:
                maximum=nums[i]

        for j in range(0,len(nums)):
            if nums[j]<maximum and nums[j]>second_largest:
                second_largest=nums[j]

        return second_largest
    
obj=Solution()
print(obj.secondLargest([100,50,40]))