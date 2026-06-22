# leetcode 66
class Solution:
    def plusOne(self, nums):
        for i in range(len(nums)-1, -1, -1):
            nums[i] += 1

            if nums[i] < 10:
                return nums

            nums[i] = 0

        return [1] + nums
# time complexity - O(n) and space complexity - O(1)
obj=Solution()
print(obj.plusOne([4,0,9]))