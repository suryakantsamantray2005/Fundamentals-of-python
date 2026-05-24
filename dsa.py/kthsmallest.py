#kth smallest in sorted matrix leetcode 378
#this can be further optimized using the concepts of heaps and binary search
class Solution:
    def kthSmallest(self,matrix,k):
        L=[]
        for i in matrix:
            for j in i:
                L.append(j)

        L.sort()

        return L[k-1]

obj=Solution()
print(obj.kthSmallest([[-5]],1))