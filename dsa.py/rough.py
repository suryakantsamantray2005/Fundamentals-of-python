#int to roman
class Solution():
    def letterCombinations(self,digits):
        dict={
            "2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"
        }
        L=[]
        if len(digits)<=4 and len(digits)>=1:
            for i in digits:
                if int(i)>=2 and int(i)<=9:
                    L.append(dict[str(i)])
                else:
                    return []

                
              

obj=Solution()
print(obj.letterCombinations("239"))