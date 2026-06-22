# permutations using the backtracking rule
class Solution:
    def permute(self,nums):
        result=[]
        def backtrack(path):
            if len(path)==len(nums):
                result.append(path[:])
                return
            for i in nums:
                if i not in path:
                    path.append(i)
                    backtrack(path)
                    path.pop()
        backtrack([])
        return result
# time complexity - 0(n*n!) and space compelxity - 0(n) excluding the output 
obj=Solution()
print(obj.permute([1,2,3]))