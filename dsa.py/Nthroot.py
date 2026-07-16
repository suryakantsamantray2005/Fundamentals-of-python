class Solution:
    def NthRoot(self, n, m):
        low=1
        high=m
        while low<=high:
            mid=(low+high)//2
            if mid**n==m:
                return mid
            elif mid**n>m:
                high=mid-1
            else:
                low=mid+1

        return -1
obj=Solution()
print(obj.NthRoot(4,81))