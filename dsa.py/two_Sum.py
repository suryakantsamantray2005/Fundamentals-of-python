# two sum leetcode 1
class Solution:
    def twoSum(self,nums,target):
        freq={}
        L=[]
        for i in range(0,len(nums)):
            if target-nums[i] not in freq:
                freq[nums[i]]=i
            else:
                L.append(freq[target-nums[i]])
                L.append(i)
        return L
    
# this is most optimized two sum problem with time complexity - O(n) and space complexity - O(n)
    
obj=Solution()
print(obj.twoSum([2,7,11,15],9))