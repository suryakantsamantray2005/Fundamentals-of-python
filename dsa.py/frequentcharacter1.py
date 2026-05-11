#finding the frequent character in the string withoiut using built-in function max
class Solution():

    def is_Frequent(self,s):
        freq={}
        for i in s:
            if s=="":
                return 0
            else:
                if i in freq:
                    freq[i]+=1
                else:
                    freq[i]=1
        max_char=''
        max_count=0
        for char, count in freq.items():  #iterate through all the key-values in a dictionary
            if count > max_count:
                max_char = char
                max_count = count

        return max_char , max_count

obj=Solution()
print(obj.is_Frequent("hello"))