# next permutations leetcode 31
class Solution:
    def nextPermutation(self,nums):
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                breakpoint=i
                break

        else:
            nums.reverse()
            return nums
        
        for j in range(len(nums)-1,breakpoint,-1):
            if nums[j]>nums[breakpoint]:
                swap_index=j
                break

        nums[swap_index],nums[breakpoint]=nums[breakpoint],nums[swap_index]

        left=breakpoint+1
        right=len(nums)-1
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
        return nums
# time complexity - O(n) and space compelexity - O(1)
obj=Solution()
print(obj.nextPermutation([2,1,5,4,3,0,0]))
