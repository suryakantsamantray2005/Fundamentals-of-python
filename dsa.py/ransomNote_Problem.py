# ransomnote problem leetcode 383
class Solution:
    def canConstruct(self,ransomNote,magazine):
        freq={}
        for i in magazine:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for j in range(0,len(ransomNote)):
            if ransomNote[j] in freq:
                if freq[ransomNote[j]]>0:
                   freq[ransomNote[j]]-=1
                else:
                    return False
            else: 
                return False
        return True
# time complexity - O(m+n) and space compelexity - O(n)
    
obj=Solution()
print(obj.canConstruct("aa","aab"))