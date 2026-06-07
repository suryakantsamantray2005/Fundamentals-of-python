# longest subarray(positive) with sum k using hashmap
class Solution:
    def longestSubArray(self,nums,k):
        prefix_sum=0
        max_len=0
        hash={}
        for i in range(0,len(nums)):
            prefix_sum=prefix_sum+nums[i]
            if prefix_sum not in hash:
                hash[prefix_sum]=i
            if prefix_sum==k:
                max_len=i+1
            rem=prefix_sum-k
            if rem in hash:
                max_len=max(max_len,i-hash[rem])
        return max_len
# time complexity - O(n) and space complexity - O(n)
obj=Solution()
print(obj.longestSubArray([1,2,3,1,1,1,1,4,2,3],3))
        
