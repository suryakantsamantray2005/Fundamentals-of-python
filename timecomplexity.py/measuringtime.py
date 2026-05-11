class Solution:

    def myAtoi(self,s):
        result=0
        result1=0
        for i in s:
            if s.startswith("-"):
                result=-(result*10+int(s[1:])) 
                return result 
            else:
                 result1=(result1*10+int(i))
                 return result1
obj=Solution()
print(obj.myAtoi("023"))