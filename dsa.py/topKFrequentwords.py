class Solution:
    def topKFrequent(self,words,k):
        freq={}
        L=[]
        M=[]
        for i in words:  #for frequency count
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1

        buckets=[[] for _ in range(0,len(words)+1)]  #creating empty buckets

        for key,value in freq.items():  #inserting the key in the respective value index
            buckets[value].append(key)

        for l in range(len(words),-1,-1):
            L.extend(sorted(buckets[l]))

        for p in range(0,k):
            M.append(L[p])
        return M
        

obj=Solution()
print(obj.topKFrequent(["aaa","aa","a"],1))