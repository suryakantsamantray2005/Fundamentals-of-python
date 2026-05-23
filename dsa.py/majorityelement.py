#majority element using boyer moore voting algorithm
class Solution:
    def majorityElement(self,arr):
       count=0
       count_1=0
       majority=None
       for i in range(0,len(arr)):
           if count==0:
               majority=arr[i]
           if arr[i]==majority:
               count=count+1
           else:
               count=count-1

       for j in range(0,len(arr)):
           if arr[j]==majority:
               count_1=count_1+1

       if count_1>len(arr)//2:
           return majority
         
obj=Solution()
print(obj.majorityElement([7,7,5,7,5,1,5,7,5,5,7,7,5,5,5,5]))