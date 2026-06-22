# rearrange characters leetcode 2287
class Solution:
    def rearrangeCharacters(self,s,target):
        freq={}
        freq1={}
        minimum=float('inf')
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for j in target:
            if j in freq1:
                freq1[j]+=1
            else:
                freq1[j]=1
        for k in set(target):
            a=freq.get(k,0)//freq1[k]
            if a<minimum:
                minimum=a
        return minimum
#time complexity - O(n) and space complexity - O(1)
obj=Solution()
print(obj.rearrangeCharacters("ilovecodingonleetcode","code"))
        