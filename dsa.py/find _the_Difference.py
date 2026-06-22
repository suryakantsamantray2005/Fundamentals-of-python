#find the difference leetcode 389
class Solution:
    def findTheDifference(self,s,t):
        count={}
        for i in t:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        for j in s:
            if j in count:
                count[j]-=1
        for key,values in count.items():
            if values==1:
                return key
# time complexity - O(n) and space complexity -O(n) if only lowercase english alphabets are allowed the space complexity will ber O(1)
obj=Solution()
print(obj.findTheDifference("abcd","abcde"))

