#insertion sort 
class Solution:
    def insertion_sort(self,arr):
        for i in range(1,len(arr)):
            if arr[i]<arr[i-1]:
                key=arr[i]
                for j in range(i,0,-1):
                    if arr[j-1]>key:
                        arr[j]=arr[j-1]
                    else:
                        arr[j]=key
                        break

                else:      # for-else condition- if loop ends naturally without break then else condition executes
                    arr[0]=key   #if loop finishes without break then else condition will execute
        return arr

obj=Solution()
print(obj.insertion_sort([3,5,6,4,8,9,10,7,1]))