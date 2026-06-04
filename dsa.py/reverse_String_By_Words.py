class Solution:
    def reverseWords(self,s):
        a=s.split()
        L=[]
        result=''
        for i in range(len(a)-1,-1,-1):
            L.append(a[i])
        result=' '.join(map(str,L))
        return result
    
#time complexity - O(2n+k) and space complexity - O(3n)


obj=Solution()
print(obj.reverseWords("the sky is blue"))