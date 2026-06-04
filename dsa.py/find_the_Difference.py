# find the difference leetcode 2215
class Solution:
    def findDifference(self,nums1,nums2):
        S1=set(nums1)
        S2=set(nums2)
        L=[]
        M=[]
        result=[]
        for i in S1:
            if i not in S2:
                L.append(i)
        for j in S2:
            if j not in S1:
                M.append(j)
        result=[L,M]
        return result
# time complexity - O(m+n) and space compplexity - O(n)
        