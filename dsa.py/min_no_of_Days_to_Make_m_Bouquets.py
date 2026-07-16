# Minimum number of days to make m bouquets leetcode 1482
class Solution:
    def minDays(self, bloomDay, m, k):
        low=min(bloomDay)
        high=max(bloomDay)
        ans=-1
        while low<=high:
            count=0
            total_bouquet=0
            mid=(low+high)//2
            for i in bloomDay:
                if mid>=i:
                    count+=1
                    if count==k:
                        total_bouquet+=1
                        count=0
                else:
                    count=0
            if total_bouquet>=m:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
# time complexity - O(nlogn) and space complexity - O(1)
obj=Solution()
print(obj.minDays([1,10,3,10,2],3,1))
            
