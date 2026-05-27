#this code is for finding third max with O(1) space complexity
class Solution:

    def thirdMax(self, nums):

        first = float('-inf')
        second = float('-inf')
        third = float('-inf')

        for num in nums:

            # skip duplicates
            if num == first or num == second or num == third:
                continue

            if num > first:

                third = second
                second = first
                first = num

            elif num > second:

                third = second
                second = num

            elif num > third:

                third = num

        # if third maximum does not exist
        if third == float('-inf'):
            return first

        return third


obj = Solution()

print(obj.thirdMax([2,2,3,1]))