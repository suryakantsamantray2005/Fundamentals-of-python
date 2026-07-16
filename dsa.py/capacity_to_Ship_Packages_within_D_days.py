# capacity to ship packages within D days leetcode 1011
class Solution:
    def shipWithinDays(self, weights, days):
        low=max(weights)
        high=sum(weights)
        while low<=high:
            total_weight=0
            count=0
            mid=(low+high)//2
            for i in weights:
                total_weight+=i
                if total_weight>mid:
                    total_weight=i
                    count+=1
            if count<days:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
# time complexity - O(nlogn) and space complexity - O(1)
obj=Solution()
print(obj.shipWithinDays([1,2,3,4,5,6,7,8,9,10],5))