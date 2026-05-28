# top lk frequent element leetcode 347
# revise this question good question
class Solution:
    def topKFrequent(self,nums,k):
        freq={}
        L=[]
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        buckets=[[] for _ in range(0,len(nums)+1)]
        for key,value in freq.items():
            buckets[value].append(key)     
        for l in range(len(nums),-1,-1):
             L.extend(buckets[l])

        return L[0:k]

obj=Solution()
print(obj.topKFrequent([1,2,1,2,1,2,3,1,3,2],2))