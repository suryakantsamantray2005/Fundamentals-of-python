# contains duplicate 2
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        hash={}
        for i in range(0,len(nums)):
            if nums[i] not in hash:
                hash[nums[i]]=i
            else:
               if i-hash[nums[i]]<=k:
                   return True
               else:
                   hash[nums[i]]=i
        return False
#revise this question
               
obj=Solution()
print(obj.containsNearbyDuplicate([1,0,1,1],1))