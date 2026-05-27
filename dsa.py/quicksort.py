#quick sort
class Solution:
    def partition(self,nums,low,high):
        pivot=nums[low]
        i,j=low,high
        while i<j:
            while nums[i]<=pivot and i<=high-1:
                i=i+1

            while nums[j]>pivot and j>=low+1:
                j=j-1

            if i<j:
                nums[i],nums[j]=nums[j],nums[i]

        nums[j],nums[low]=nums[low],nums[j]

        return j
    
    def quick_sort(self,nums,low,high):
        if low<high:
            p_index=self.partition(nums,low,high)
            self.quick_sort(nums,low,p_index-1)
            self.quick_sort(nums,p_index+1,high)
        return nums
obj=Solution()
nums=[4,1,7,6,3,2,8]
print(obj.quick_sort(nums,0,len(nums)-1))
