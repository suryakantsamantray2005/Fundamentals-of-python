#squares of sorted array
#Input: nums = [-4,-1,0,3,10]
#Output: [0,1,9,16,100]
#Explanation: After squaring, the array becomes [16,1,0,9,100].
#After sorting, it becomes [0,1,9,16,100].
class Solution:
    def sortedSquares(self,nums):
        L=[]
        for i in nums:
            L.append(i**2)

        for j in range(len(L)):
            minimum=j
            for k in range(j+1,len(L)):
                if L[k]<L[minimum]:
                    minimum=k
            L[j],L[minimum]=L[minimum],L[j]

        return L
    

#this has time complexity O(N^2) which has runtime error in leetcode 

obj=Solution()
print(obj.sortedSquares([-4,-1,0,3,10]))