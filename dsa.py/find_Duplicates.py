#find duplicate leetcode 442 
class Solution:
    def findDuplicates(self,nums):
        freq={}
        L=[]
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1

        for key, value in freq.items():
            if value>=2:
                L.append(key)
        return L
    
#it has time and space complexity O(n) excluding result 
# so it further optimized to O(1) space complexity excluding result
obj=Solution()
print(obj.findDuplicates([9,2,1]))