#merge sort 
class Solution:
    def merge_array(self,left,right):
        result=[]
        i,j=0,0
        n,m=len(left),len(right)
        while i<n and j<m:
            if left[i]<=right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        while j<m:
                result.append(right[j])
                j=j+1
        while i<n:
               result.append(left[i])
               i=i+1

        return result

    def merge_sort(self,arr):
        if len(arr)<=1:
            return arr
        mid=len(arr)//2
        left_arr=arr[:mid]
        right_arr=arr[mid:]
        left_half=self.merge_sort(left_arr)
        right_half=self.merge_sort(right_arr)
        return self.merge_array(left_half,right_half)

obj=Solution()
print(obj.merge_sort([3,1,2,4,1,5,2,6,4]))