# rearrange arrays leetcode 2149
class Solution:
    def rearrangeArray(self,nums):
        L=[0]*len(nums)
        posindex=0
        negindex=1
        for i in range(0,len(nums)):
            if nums[i]>0:
                L[posindex]=nums[i]
                posindex+=2
            else:
                L[negindex]=nums[i]
                negindex+=2
        return L
#time complexity - O(n) and space complexity - O(n)