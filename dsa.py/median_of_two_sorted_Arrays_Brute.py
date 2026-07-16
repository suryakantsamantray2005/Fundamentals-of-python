# median of two sorted arrays brute solution
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        i,j=0,0
        L=[]
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<=nums2[j]:
                L.append(nums1[i])
                i+=1
            else:
                L.append(nums2[j])
                j+=1
        while j<len(nums2):
            L.append(nums2[j])
            j+=1
        while i<len(nums1):
            L.append(nums1[i])
            i+=1
        if len(L)%2==0:
            return float(L[(len(L)-1)//2]+L[(len(L)//2)])/2
        else:
            return float(L[len(L)//2])
# time complexity - O(n) and space complexity - O(1)
obj=Solution()
print(obj.findMedianSortedArrays([2,3,6,15],[1,3,4,7,10]))