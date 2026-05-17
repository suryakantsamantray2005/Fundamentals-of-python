#merge sort array
class Solution():
    def merge(self,nums1,m,nums2,n):
        L=[]
        for i in range(m):
           L.append(nums1[i])

        for j in range(n):
            L.append(nums2[j])

        for k in range(0,len(L)-1):
            minimum=k

            for l in range(k+1,len(L)):
              if L[l]<L[minimum]:
                minimum=l

            temp=L[k]
            L[k]=L[minimum]
            L[minimum]=temp

        
        for m in range(len(L)):
            nums1[m]=L[m]
       
    
obj=Solution()
print(obj.merge([1,2,3,0,0,0],3,[2,5,6],3))