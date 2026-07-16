# find smallest letter greater than target leetcode 744 
# simple problem of upper bound case
class Solution:
    def nextGreatestLetter(self, letters, target):
        low=0
        high=len(letters)-1
        ans=letters[0]
        while low<=high:
            mid=(low+high)//2
            if ord(letters[mid])>ord(target):
                ans=letters[mid]
                high=mid-1
            else:
                low=mid+1
        return ans
# time complexity - O(logn) and space complexity - O(1)
obj=Solution()
print(obj.nextGreatestLetter(["c","f","j"],"k"))