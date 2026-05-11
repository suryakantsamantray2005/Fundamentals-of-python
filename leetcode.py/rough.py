class Solution:

    def isPalindrome(self,x):
        if x>=0:
            original=x
            rev=0
            while x!=0:
                rev=rev*10+x%10
                x=x//10
            if original==rev:
                return True
            else:
                return False
        else:
            return False
        
obj=Solution()
print(obj.isPalindrome(0))