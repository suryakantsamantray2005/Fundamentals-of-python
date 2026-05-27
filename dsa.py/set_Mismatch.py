#set mismatch leetcode no 645
class Solution:
    def findErrorNums(self,nums):
        freq={}
        L=[]
        for i in nums:  # for duplicates
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for key,value in freq.items():
            if value==2:
                L.append(key)
        S1=set(nums)
        for j in range(1,len(nums)+1):
            if j not in S1:
                L.append(j)
        return L