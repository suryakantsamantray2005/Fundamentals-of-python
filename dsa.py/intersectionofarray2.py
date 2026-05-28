class Solution:
    def intersect(self,nums1,nums2):
        D=tuple(nums2)
        L=[]
        for i in nums1:
            if i in D:
                L.append(i)

        return L

obj=Solution()
print(obj.intersect([1,2,2,1],[2,2]))