class Solution():
    def sorting(self,arr):
        for i in range(0,len(arr)-1):   #because last element is already sorted
            minimum=i                   #assuming the minimum is first element
            for j in range(i+1,len(arr)): 
                if arr[j]<arr[minimum]:  #if assuming element is bigger than j element make minimum than j element and continue the loop
                    minimum=j

            temp=arr[i]     #swaping of that minimum and first index element according to i
            arr[i]=arr[minimum]
            arr[minimum]=temp

        return arr

        
obj=Solution()
print(obj.sorting([5,7,8,4,1,6,9,2]))