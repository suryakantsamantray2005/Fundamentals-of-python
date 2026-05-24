#anagram leetcode 242
class Solution:
    def isAnagram(self,s,t):
        if sorted(s)==sorted(t):
            return True
        else:
            return False
obj=Solution()
print(obj.isAnagram("ab","a"))