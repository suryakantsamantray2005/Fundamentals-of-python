#frequency sort leetcode 451
# time complexity = O(n) and space complexity = O(n)
#complete this after learning bucket sort
class Solution:
    def frequenctSort(self,s):
        freq={}
        result=''
        maximum=float('-inf')
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1

        for key,value in freq.items():
            if value>maximum:
                maximum=value
                

obj=Solution()
print(obj.frequenctSort("tree"))