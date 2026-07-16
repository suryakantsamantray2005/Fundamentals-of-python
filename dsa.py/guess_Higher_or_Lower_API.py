# guess number higher or lower leetcode 374
class Solution:
    def guessNumber(self,n):
        low=1
        high=n
        while low<=high:
            mid=(low+high)//2
            result=guess(mid)
            if result==0:
                return mid
            elif result==-1:
                high=mid-1
            else:
                low=mid+1
# it teaches that binary search is not limited to sorted array it can be implement to 
# any search space like this question