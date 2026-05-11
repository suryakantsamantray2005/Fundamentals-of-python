#Finding the first non repeating character in the string
class Solution():
    def firstUniqChar(self,s):
      dict={}
      for i in s:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1

      for j in range(len(s)):
        if dict[s[j]]==1:
            return j
      return -1
obj=Solution()
print(obj.firstUniqChar("loveleetcode"))