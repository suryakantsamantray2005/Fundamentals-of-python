#string compression
#ex. input - "aaabbcc"
#output - "a3b2c2"
class Solution():

    def string_Compression(self,s):
        result=''
        count=1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                count+=1
            else:
                result=result+s[i-1]+str(count)
                count=1
        result=result+s[-1]+str(count)

        return result
    
obj=Solution()
print(obj.string_Compression("aaabbccceefff"))