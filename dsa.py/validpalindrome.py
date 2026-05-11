#A phrase is a palindrome if, after converting all uppercase 
#letters into lowercase letters and removing all non-alphanumeric characters, 
#it reads the same forward and backward. Alphanumeric characters include letters and numbers.
#eg. Input: s = "A man, a plan, a canal: Panama"
#Output: true
#Explanation: "amanaplanacanalpanama" is a palindrome.
class Solution():

    def isPalindrome(self,s):
        result=''
        for i in s:
            if i.isalnum():
                a=i.lower()
                result=result+a
        
        b=result[::-1]
        if b==result:
            return True
        else:
            return False
        
obj=Solution()
print(obj.isPalindrome("A man, a plan, a canal: Panama"))