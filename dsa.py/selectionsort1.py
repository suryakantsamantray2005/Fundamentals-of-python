#sorting in decreasing order
class Solution:
    def sorting_in_Decreasing(self,arr):
        for i in range(len(arr)-1):
            maximum=i
            for j in range(i+1,len(arr)):
                if arr[j]>arr[maximum]:
                    maximum=j

            temp=arr[i]
            arr[i]=arr[maximum]
            arr[maximum]=temp
        return arr

obj=Solution()
print(obj.sorting_in_Decreasing([2,7,9,4,6,0]))