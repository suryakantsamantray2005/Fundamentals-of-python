class Solution():
    
    def is_Palindrome(self,s):
        i=0
        j=len(s)-1

        while i<j:
            if s[i]!=s[j]:
                return False
            
            i+=1
            j-=1

        return True
    
obj=Solution()
print(obj.is_Palindrome('madam'))