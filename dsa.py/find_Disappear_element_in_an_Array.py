# Find all disappear number in an array leetcode 448
class Solution:
    def findDisappearedNumbers(self, nums):
        L=[]
        for i in nums:
            index=abs(i)-1
            nums[index]=-abs(nums[index]) # always make the element negative
        for i in range(0,len(nums)):
            if nums[i]>0:
                L.append(i+1)
        return L
# time complexity - O(n) and space complexity - O(1)
obj=Solution()
print(obj.findDisappearedNumbers([4,3,2,7,8,2,3,1]))