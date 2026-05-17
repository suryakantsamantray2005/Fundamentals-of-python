class Solution:
    def merge(self, nums1, m, nums2, n):

        L = []

        for i in range(m):
            L.append(nums1[i])

        for j in range(n):
            L.append(nums2[j])

        # Selection Sort
        for k in range(len(L)-1):

            minimum = k

            for l in range(k+1, len(L)):

                if L[l] < L[minimum]:
                    minimum = l

            L[k], L[minimum] = L[minimum], L[k]

        # Copy into nums1
        for i in range(len(L)):
            nums1[i] = L[i]

        return nums1

obj=Solution()
print(obj.merge([1,2,3,0,0,0],3,[2,5,6],3))