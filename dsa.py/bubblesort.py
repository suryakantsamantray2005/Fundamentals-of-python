# bubble sort
class Solution:
    def bubble_sort(self,arr):  #here we compare the adjacent elements if adjacent element bigger then swap
        for i in range(0,len(arr)):
            for j in range(0,len(arr)-1-i):   # the last element is already sort so it is excluded from the loop
                maximum=j+1
                if arr[j]>arr[maximum]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]


        return arr




obj=Solution()
print(obj.bubble_sort([2,7,4,9,1,5,0]))