#separate the digits in an array 
class Solution():

    def separateDigits(self,nums):
      result = [int("".join(map(str, nums)))]
      L=[]
      for i in result:
         while i!=0:
           rev=i%10
           i=i//10
           L.append(rev)
      
      for j in L:
         a=L[::-1]

      return a
    
obj=Solution()
print(obj.separateDigits([13,25,83,77]))