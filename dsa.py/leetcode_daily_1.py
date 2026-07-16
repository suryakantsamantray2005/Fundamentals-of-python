# leetcode 1846
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self,arr):
        arr.sort()
        if arr[0]!=1:
            arr[0]=1
        for i in range(1,len(arr)):
            if arr[i]-arr[i-1]>1:
                arr[i]=arr[i-1]+1
        return arr[-1]
    
obj=Solution()
print(obj.maximumElementAfterDecrementingAndRearranging([100,1,1000]))