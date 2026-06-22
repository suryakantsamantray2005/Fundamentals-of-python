# longest consecutive lenght leetcode 128
class Solution:
    def longestConsecutive(self,nums):
        if len(nums)==0:
            return 0
        S=set(nums)
        count=1
        max_count=1
        for i in S:
            if i-1 in S:
                continue
            while i+1 in S:
                count+=1
                i+=1
            max_count=max(max_count,count)
            count=1
        return max_count
# time complexity - O(n) and space complexity - O(n)
obj=Solution()
print(obj.longestConsecutive([0]))
