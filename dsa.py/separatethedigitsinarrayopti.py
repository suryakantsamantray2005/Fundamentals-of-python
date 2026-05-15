#this is the optimal code of the separating the digits in array question
class Solution:

    def separateDigits(self, nums):
        result = []

        for num in nums:
            for digit in str(num):
                result.append(int(digit))

        return result


obj = Solution()
print(obj.separateDigits([12,22,45,790]))