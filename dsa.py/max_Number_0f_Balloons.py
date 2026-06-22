# maximum number of balloons 1189
class Solution:
    def maxNumberOfBalloons(self,text):
        freq={}
        for i in text:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1

        return min(freq.get('b',0)//1,freq.get('a',0)//1,freq.get('l',0)//2,freq.get('o',0)//2,freq.get('n',0)//1)
# time complexity - O(n) and space complexity - O(1) because frequency only stores the 26 distinct lowercase alphabets
obj=Solution()
print(obj.maxNumberOfBalloons("nlaebolko"))
        