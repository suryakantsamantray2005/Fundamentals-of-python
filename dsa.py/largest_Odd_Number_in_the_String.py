# Largest odd number in the string leetcode 1903
class Solution:
    def largestOddNumber(self, num):
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2==1:
                return num[0:i+1]
        return ""
# time complexity - O(n) and space complexity - O(1)
obj=Solution()
print(obj.largestOddNumber("420"))