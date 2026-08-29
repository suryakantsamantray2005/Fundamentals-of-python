# Maximum product of two digit leetcode 3536
class Solution:
    def maxProduct(self,n):
        max_digit=float('-inf')
        sec_max=float('-inf')
        while n!=0:
            digit=n%10
            if digit>=max_digit:
                sec_max=max_digit
                max_digit=digit
            elif digit<max_digit and digit>sec_max:
                sec_max=digit
            n=n//10
        return max_digit*sec_max
# time complexity - O(logn) and space compelxity - O(1)
obj=Solution()
print(obj.maxProduct(122))