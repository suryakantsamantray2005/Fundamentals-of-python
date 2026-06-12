# sort colors leetcode 75
class Solution:
    def dutchnationalflagAlgo(self,nums):
        low,mid=0,0
        high=len(nums)-1
        while mid<=high:
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
        return nums
# tinme complexity - O(n) and space complexity - O(1)
obj=Solution()
print(obj.dutchnationalflagAlgo([0,1,1,0,1,2,1,2,0,0,0]))