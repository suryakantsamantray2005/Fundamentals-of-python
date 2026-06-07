# xor method for finding the single repeated number 
class Solution:
    def singleNumbewr(self,nums):
        result=0
        for i in nums:
            result=result^i
        return result
# it is most optimal way having time complexity - O(n) and space complexity -O(1) 
obj=Solution()
print(obj.singleNumbewr([1,1,2,3,3,4,4]))