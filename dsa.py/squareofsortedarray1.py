class Solution:
    def sortedsquares(self,nums):
        L=[]
        for i in nums:
            L.append(i**2)

        L.sort()
        return L
    
#this has time complexity has O(N logN)  (it is accepted by leetcode)
# because python built in sort function has this time complexity the built-in sort uses Timsort sorting
# which is the combination of merge sort and insertion sort
    
obj=Solution()
print(obj.sortedsquares([-4,-1,0,3,10]))