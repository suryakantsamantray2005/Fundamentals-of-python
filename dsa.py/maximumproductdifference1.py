import time
start=time.time()
class Solution:
    def maxProductDifference(self,nums):
        if nums[0]>nums[1]:
            largest=nums[0]
            second_largest=nums[1]
            smallest=nums[1]
            second_smallest=nums[0]
        else:
            largest=nums[1]
            second_largest=nums[0]
            smallest=nums[0]
            second_smallest=nums[1]
        for i in range(2,len(nums)):
            if nums[i]>largest:
                second_largest=largest
                largest=nums[i]
            elif nums[i]>second_largest:
                second_largest=nums[i]
            elif nums[i]<smallest:
                second_smallest=smallest
                smallest=nums[i]
            elif nums[i]<second_smallest:
                second_smallest=nums[i]

            product=largest*second_largest-smallest*second_smallest

        return product
#this is optimized solution because it has the time complexity of O(N)   
end=time.time()
print(end-start)

obj=Solution()
print(obj.maxProductDifference([2,5,9,1]))