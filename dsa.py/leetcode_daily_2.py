class Solution:
    def numOfStrings(self,patterns,word):
        count=0
        for i in patterns:
            if i in word:
                count+=1

        return count
# time comeplexity - O(n*m*k) the extra k comes from the substring search in the word
#  space complexity - O(1) 
obj=Solution()
print(obj.numOfStrings(["ab", "aa", "bb"],"aaaaabbbbb"))