# sequential digits leetcode 1291
class Solution:
    def sequentialDigits(self, low, high):
        s="123456789"
        L=[]
        for i in range(0,len(s)):
            for j in range(i+1,len(s)+1):
                if low<=int(s[i:j])<=high:
                    L.append(int(s[i:j]))
                elif int(s[i:j])>high:
                    break
        L.sort()
        return L
# time complexity - O(1) since there are only some constant iteration 
# space compexity - O(1) excluding the output space
obj=Solution()
print(obj.sequentialDigits(1000,13000))