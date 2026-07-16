# median of two sorted array leetcode 4
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        length=len(nums1)+len(nums2)
        if length%2==0:
            low=0
            high=len(nums1)
            partition=length//2
            while low<=high:
                cut1=(low+high)//2
                cut2=partition-cut1
                left1=float('-inf') if cut1==0 else nums1[cut1-1]
                right1=float('inf') if cut1==len(nums1) else nums1[cut1]
                left2=float('-inf') if cut2==0 else nums2[cut2-1]
                right2=float('inf') if cut2==len(nums2) else nums2[cut2]
                if left1<=right2 and left2<=right1:
                    return float(max(left1,left2)+min(right1,right2))/2
                elif left1>right2:
                    high=cut1-1
                else:
                    low=cut1+1
        else:
            low=0
            high=len(nums1)
            partition=(length+1)//2
            while low<=high:
                cut1=(low+high)//2
                cut2=partition-cut1
                left1=float('-inf') if cut1==0 else nums1[cut1-1]
                right1=float('inf') if cut1==len(nums1) else nums1[cut1]
                left2=float('-inf') if cut2==0 else nums2[cut2-1]
                right2=float('inf') if cut2==len(nums2) else nums2[cut2]
                if left1<=right2 and left2<=right1:
                    return float(max(left1,left2))
                elif left1>right2:
                    high=cut1-1
                else:
                    low=cut1+1
# time complexity - O(log(min(m,n))) and space complexity - O(1)
obj=Solution()
print(obj.findMedianSortedArrays([7,12,14],[1,2,3,4,9,11]))
