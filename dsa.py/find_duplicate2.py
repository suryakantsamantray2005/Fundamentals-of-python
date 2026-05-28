#find duplicate
class Solution:
    def findDuplicates(self, nums):
        result = []

        for i in nums:
            index = abs(i) - 1

            if nums[index] < 0:
                result.append(abs(i))
            else:
                nums[index] = -nums[index]

        return result
#it has time complexity O(n) but space complexity O(1) excluding result


obj = Solution()
print(obj.findDuplicates([3,2,1,2]))