class Solution:
    def frequencySort(self,s):
        L=[]
        M=[]
        freq={}
        result=''
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1

        buckets=[[] for _ in range(0,len(s)+1)]
        for key,value in freq.items():
            buckets[value].append(key)
        for j in range(len(s),-1,-1):
            L.extend(buckets[j])
        for k in L:
            M.append(k*freq[k])
        
        return "".join(M)
obj=Solution()
print(obj.frequencySort("tree"))