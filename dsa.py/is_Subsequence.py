# isSubsequence leetcode 392
class Solution(object):
    def isSubsequence(self, s, t):
        count=0
        i,j=0,0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
                j+=1
                count+=1
            else:
                j+=1
        if count==len(s):
            return True
        else:
            return False
# this question is done by using the two pointer approach
# time complexity - O(n) and space complexity - O(1)