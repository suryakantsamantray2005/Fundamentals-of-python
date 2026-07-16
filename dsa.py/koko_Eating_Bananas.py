# koko eating bananas leetcode 875
class Solution:
    def minEatingSpeed(self, piles, h):
        low=1
        high=max(piles)
        while low<=high:
            ceil=0
            mid=(low+high)//2
            for i in piles:
                j=i//mid
                if i%mid!=0:
                    j+=1
                ceil=ceil+j
            if ceil<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1

        return ans
# time complexity - O(nlogm) and space complexity - O(1)
obj=Solution()
print(obj.minEatingSpeed([3,6,7,11],8))