# seach in 2-D matrix-II leetcode 240
class Solution:
    def searchMatrix(self, matrix, target):
        row=0
        col=len(matrix[0])-1
        while row<len(matrix) and col>=0:
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:
                col-=1
            else:
                row+=1
        return False
# time complexity is O(m+n) check how many time the row and col moves row increases m times 
# and col decreases n times space complexity - O(1)
obj=Solution()
print(obj.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],14))