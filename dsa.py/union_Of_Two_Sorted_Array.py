# union of two sorted array
class Solution:
    def union(self,arr1,arr2):
        L=[]
        i,j=0,0
        while i<len(arr1) and j<len(arr2):
              if arr1[i]<arr2[j]:
                   if len(L)==0 or L[-1]!=arr1[i]:
                        L.append(arr1[i])
                   i=i+1
              elif arr1[i]>arr2[j]:
                   if len(L)==0 or L[-1]!=arr2[j]:
                        L.append(arr2[j])
                   j=j+1
              else:
                   if len(L)==0 or L[-1]!=arr1[i]:
                        L.append(arr1[i]) 
                   i=i+1
                   j=j+1

        while i<len(arr1):
             if len(L)==0 or L[-1]!=arr1[i]:
                  L.append(arr1[i])
             i=i+1
        while j<len(arr2):
             if len(L)==0 or L[-1]!=arr2[j]:
                  L.append(arr2[j])
             j=j+1
        return L
    
#time complexity - O(m+n) space complexity - O(m+n)       
obj=Solution()
print(obj.union([1,1,2,3,4,5],[2,3,4,4,5,6]))