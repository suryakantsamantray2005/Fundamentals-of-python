class Computational:

    def __init__(self):
        pass

    def Factorial(self,n):     #function for factorial
        product=1
        for i in range(1,n+1):
            product=product*i
        print('the factorial of',n,'is',product)

    def natural_sum(self,n):   #function for sum of natural numbers
        total=(n*(n+1))//2
        print('the sum of',n,'is',total)

    def test_prime(self, n):   #function for checking prime integer

     if n<= 1:
        print("the integer is not prime")

     else:
        flag = True

        for i in range(2, n):
            if n % i == 0:
                flag = False
                break

        if flag == True:
            print("integer is prime")
        else:
            print("integer is not prime")

    def test_prims(self,n1,n2):  #function for checking co-prime
        for i in range(min(n1,n2),0,-1):
            if n1%i==0 and n2%i==0:
                if i==1:
                  print('it is co-prime')
                else:
                  print('it is not co-prime')
                break

    def table_Mult(self,n):      #Multiplication of integer upto 10
        L=[]
        for i in range(1,11):
            L.append(n*i)
        return L

    def list_Div(self,n):        #get divisors of a integer
        L=[]
        for i in range(1,n+1):
            if n%i==0:
                L.append(i)
        return L

    def list_prime_Div(self,n): #get prime divisors of a integer
        L=[]
        M=[]
        for i in range(1,n+1):
            if n%i==0:
                L.append(i)

        for j in L:
            if j>1:
             flag = True
             for k in range(2,j):
                if j%k==0:
                 flag = False
                 break
             if flag:
               M.append(j)
        return M
                    


test1 = Computational()
print(test1.list_Div(12))