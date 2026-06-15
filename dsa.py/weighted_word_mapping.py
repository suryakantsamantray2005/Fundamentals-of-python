# leetcode 3838
class Solution:
    def mapWordWeights(self,words,weights):
        hash={}
        alpha=97
        intmap=0
        summ=0
        result=''
        while alpha<=122 and intmap<=25:
           hash[chr(alpha)]=weights[intmap]
           alpha+=1
           intmap+=1
        for i in words:
            for j in i:
                summ=summ+hash[j]
            a=summ%26
            result=result+chr(122-a)
            summ=0
        return result
# time complexity - O(n) and space complexity - O(1) excluding output space
obj=Solution()
print(obj.mapWordWeights(["abcd","def","xyz"],[5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]))