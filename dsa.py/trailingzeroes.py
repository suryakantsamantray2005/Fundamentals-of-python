#Trailing zeroes
class Solution():
    def trailingZeroes(self,n):
        product=1
        L=[]
        count=0
        for i in range(1,n+1):
            product=product*i

        a=str(product)
        for j in a[::-1]:
            L.append(j)

        for k in L:
            if  int(k)==0:
                count=count+1

            else:
                break

        return count


obj=Solution()
print(obj.trailingZeroes(7))