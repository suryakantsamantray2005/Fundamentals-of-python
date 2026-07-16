# find the row index with the maximum no of 1's
class Solution:
    def rowWithMax1s(self, mat):
       index=-1
       totalones=0
       for i in range(0,len(mat)):
           low=0
           high=len(mat[i])-1
           lenofarray=len(mat[i])
           while low<=high:
               mid=(low+high)//2
               if mat[i][mid]==1:
                   ones=lenofarray-mid
                   if ones>totalones:
                       totalones=ones
                       index=i
                   high=mid-1
               else:
                   low=mid+1
       return index
# time complexity - O(nlogm) and space complexity - O(1)
obj=Solution()
print(obj.rowWithMax1s([ [1, 1, 1], [0, 0, 1], [0, 0, 0]]))
