#bucket sort 
class Solution:
    def bucketSort(self,nums):
        buckets=[[] for _ in range(0,len(nums))]  #buckets created according to length of array
        for i in nums:  #insering elements in buckets
            index=int(i*len(nums))
            buckets[index].append(i)

        for j in buckets:  #sorting elements inside bucket
            j.sort()

        result=[]

        for j in buckets:  #merging all buckets
            result.extend(j)
        return result
    
obj=Solution()
print(obj.bucketSort([0.29,0.39,0.41,0.15]))