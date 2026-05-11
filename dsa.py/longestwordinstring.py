#finding the longest word in a string
#ex. input - "I love python programming"
# output - "programing"
class Solution:

    def long_String(self,s):
        a=s.split()
        count=0
        max_char=''
        for i in a:
            if len(i)>count:
                count=len(i)
                max_char=i

        return max_char, count

    
obj=Solution()
print(obj.long_String("I love python programming"))