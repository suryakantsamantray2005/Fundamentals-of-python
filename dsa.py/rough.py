import time
start=time.time()
class Solution:
    def maxProductDifference(self,nums):
        L=[]
        a=max(nums)
        L.append(a)
        nums.remove(a)
        b=max(nums)
        L.append(b)
        nums.remove(b)
        c=min(nums)
        L.append(c)
        nums.remove(c)
        d=min(nums)
        L.append(d)
        product=L[0]*L[1]-L[2]*L[3]
        return product
    
end=time.time()
print(end-start)
    
obj=Solution()
print(obj.maxProductDifference([2,5,9,1]))