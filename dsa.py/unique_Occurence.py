# unique occurence leetcode 1207
class Solution(object):
    def uniqueOccurrences(self, arr):
        freq={}
        S1=set(arr)
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        S2=set(freq.values())
        if len(S1)==len(S2):
            return True
        else:
            return False
        
# time complexity - O(n) and space complexity - O(n)
        

obj=Solution()
print(obj.uniqueOccurrences([1,2,2,1,1,3]))