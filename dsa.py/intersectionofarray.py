class Solution:
    def intersection(self,nums1,nums2):
        S=set(nums2)
        S1=set()
        for i in nums1:
            if i in S:
                S1.add(i)
        return list(S1)

obj=Solution()
print(obj.intersection([1,2,2,1],[2,2]))