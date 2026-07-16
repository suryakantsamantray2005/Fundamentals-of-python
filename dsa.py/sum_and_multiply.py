class Solution:
    def sumAndMultiplyrecursion(self, string_int):
        n=int(string_int)
        unit_place=1
        ans=0
        total_sum=0
        while n!=0:
            last_digit=n%10
            if last_digit!=0:
                ans=unit_place*last_digit+ans
                unit_place=unit_place*10
                total_sum=total_sum+last_digit
            n=n//10
        final_ans=ans*total_sum
        return final_ans

    def sumAndMultiply(self,s,queries):
        L=[]
        for i in range(0,len(queries)):
            result=self.sumAndMultiplyrecursion(s[queries[i][0]:queries[i][1]+1])
            L.append(result%(10**9+7))
        return L
obj=Solution()
print(obj.sumAndMultiply("10203004",[[0,7],[1,3],[4,6]]))