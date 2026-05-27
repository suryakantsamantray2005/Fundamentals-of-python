class Solution:
    def thirdMax(self,nums):
        maximum=nums[0]
        second_maximum=float('-inf')
        third_maximum=float('-inf')
        for i in range(0,len(nums)):
            if nums[i]>maximum:
                maximum=nums[i]
        for j in range(0,len(nums)):
            if nums[j]<maximum and second_maximum<nums[j]:
                second_maximum=nums[j]

        for k in range(0,len(nums)):
            if nums[k]<maximum and nums[k]<second_maximum and third_maximum<nums[k]:
                third_maximum=nums[k]
        L=list(set(nums))
        if len(L)<3:
            return maximum
        else:
            return third_maximum
        
obj=Solution()
print(obj.thirdMax([3,2,1]))