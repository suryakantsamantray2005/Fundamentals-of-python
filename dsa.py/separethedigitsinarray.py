#separate the digits in an array 
class Solution():

    def separateDigits(self,nums):
      L=[]
      for i in nums:
         while i!=0:
            rev=i%10
            i=i//10
            L.append(rev)

      return L
    
obj=Solution()
print(obj.separateDigits([13,14,15]))