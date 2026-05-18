#3 Sum
class Solution:
    def threeSum(self,nums):
        L=[]
        M=[]
        for i in range(len(nums)):
           for j in range(i+1,len(nums)):
               for k in range(j+1,len(nums)):
                   if nums[i]+nums[j]+nums[k]==0:
                     L.append([nums[i],nums[j],nums[k]])
        for l in L:
            l.sort() 

        for m in L:
            if m not in M:
                M.append(m)

        return M

obj=Solution()
print(obj.threeSum([0,1,1]))