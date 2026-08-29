# Smallest divisible digit product I Leetcode 3345
class Solution:
    def smallestNumber(self, n, t):
        while n<=100:
            rev=1
            i=n
            while i!=0:
                rev=rev*(i%10)
                i=i//10
            if rev%t==0:
                return n
            else:
                n+=1
# effectively the time complexity is O(1) and the constriants is between 1<=n<=100 and 
# space comeplxity - O(1)
obj=Solution()
print(obj.smallestNumber(15,3))