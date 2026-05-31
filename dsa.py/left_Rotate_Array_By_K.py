#left rotation array
class Solution:
    def rotate(self,nums,k):
        k=k%len(nums)
        temp=nums[0:k]
        l=0
        for i in range(k,len(nums)):
            nums[i-k]=nums[i]

        for j in range(len(nums)-k,len(nums)):
            nums[j]=temp[l]
            l+=1
        return nums
    
#it has time complexity - O(n) and space complexity - O(n)
obj=Solution()
print(obj.rotate([1,2,3,4,5,6,7],8))