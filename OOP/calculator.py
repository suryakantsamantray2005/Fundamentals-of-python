class Calculator:

    def __init__(self):
        self.history=[]

    def menu(self):
        while True:
            print("="*40)
            print("      WELCOME TO SMART CALCULATOR")
            print("="*40)
            self.user_input=int(input('''
              Select which calculator do you want
              1. Basic Calculator
              2. Scientific calculator
              3. Finance Calculator
              4. Unit Converter
              5. Health Calculator
              6. Exit
                Enter your choice
              ''')
            )
            if self.user_input==1:
                user_input2=int(input('''
              What operation do you want to perform
                1. Addition
                2. Subtraction
                3. Multiplication
                4. Division                  
                                  ''')
                )
                if user_input2==1:
                    a=float(input("enter first number "))
                    b=float(input("enter second number "))
                    result=self.addition(a,b)
                    print(result)

                elif user_input2==2:
                    a=float(input("enter first number "))
                    b=float(input("enter second number "))
                    result=self.subtraction(a,b)
                    print(result)

                elif user_input2==3:
                    a=float(input("enter first number "))
                    b=float(input("enter second number "))
                    result=self.multiplication(a,b)
                    print(result)

                elif user_input2==4:
                    a=float(input("enter first number "))
                    b=float(input("enter second number "))
                    if b!=0:
                        result=self.division(a,b)
                        print(result)
                    else:
                        print("cannot divide by zero")
                else:
                    print("INVALID INPUT")



            elif self.user_input==2:
                user_input3=int(input('''
             What operation do you want to perform
                1. Square
                2. Square Root
                3. Power
                4. Factorial
                                      '''))
                
                if user_input3==1:
                    a=float(input("enter the number "))
                    result=self.square(a)
                    print(result)

                elif user_input3==2:
                    a=float(input("enter the number "))
                    result=self.squareroot(a)
                    print(result)

                elif user_input3==3:
                    a=float(input("enter the base "))
                    b=float(input("enter exponent "))
                    result=self.power(a,b)
                    print(result)

                elif user_input3==4:
                    a=int(input("enter the number "))
                    if a>=0:
                      result=self.factorial(a)
                      print(result)
                    else:
                        print("Factorial integer cannot be negative")

                else:
                    print("INVALID INPUT")
                
            elif self.user_input==3:
                user_input4=int(input('''
             What operation do you want to perform
                1. Percentage
                2. GST
                3. Discount
                                      '''))
                if user_input4==1:
                    a=float(input("enter total number "))
                    b=float(input("enter percent value "))
                    result=self.percentage(a,b)
                    print(result)

                elif user_input4==2:
                    a=float(input("enter the original amount "))
                    b=float(input("enter gst percentage "))
                    result=self.gst(a,b)
                    print("total amount with gst is" ,result)

                elif user_input4==3:
                    a=float(input("enter the original price "))
                    b=float(input("enter discount percent "))
                    discount_amount,amount_after_discount=self.discount(a,b)
                    print("Discount amount is",amount_after_discount)
                    print("Price after discount is",discount_amount)

                
            elif self.user_input==4:
                user_input5=int(input('''
              What operation do you want to perform
                1. Temperature converter
                2. Length
                3. Weight
                                       '''))
                
                if user_input5==1:
                    user_inputX=int(input('''
              Enter choice 
                1. Degree celsius to fahreneit
                2. Fahreneit to degree celcius
                3. Degree celcius to Kelvin
                4. Kelvin to degree celsius
                                          '''))
                    if user_inputX==1:
                        a=float(input("enter value "))
                        result=self.degree_to_fah(a)
                        print(result)

                    elif user_inputX==2:
                        a=float(input("enter the value "))
                        result=self.fah_to_degree(a)
                        print(result)

                    elif user_inputX==3:
                        a=float(input("enter the value "))
                        result=self.degree_to_kelv(a)
                        print(result)

                    elif user_inputX==4:
                        a=float(input("enter the value "))
                        result=self.kelv_to_degree(a)
                        print(result)

                    else:
                        print("INVALID INPUT")

                elif user_input5==2:
                    user_inputY=int(input('''
              Enter Choice
              1. meter to kilometer
              2. kilometer to meter
              3. centimeter to meter
              4. meter to centimeter
              5. centimeter to millimeter
              6. millimeter to centimeter
              7. inch to centimeter
              8. foot to meter
                                          '''))
                    
                    if user_inputY==1:
                        a=float(input("enter the value "))
                        result=self.m_to_km(a)
                        print(result)

                    elif user_inputY==2:
                        a=float(input("enter the value "))
                        result=self.km_to_m(a)
                        print(result)

                    elif user_inputY==3:
                        a=float(input("enter the value "))
                        result=self.cm_to_m(a)
                        print(result)

                    elif user_inputY==4:
                        a=float(input("enter the value "))
                        result=self.m_to_cm(a)
                        print(result)

                    elif user_inputY==5:
                        a=float(input("enter the value "))
                        result=self.cm_to_mm(a)
                        print(result)

                    elif user_inputY==6:
                        a=float(input("enter the value "))
                        result=self.mm_to_cm(a)
                        print(result)

                    elif user_inputY==7:
                        a=float(input("enter the value "))
                        result=self.inch_to_cm(a)
                        print(result)

                    elif user_inputY==8:
                        a=float(input("enter the value "))
                        result=self.foot_to_m(a)
                        print(result)

                    else:
                        print("INVALID INPUT")
                
                elif user_input5==3:
                    user_inputZ=int(input('''
                
              1. Kilogram to Gram
              2. Gram to Kilogram
              3. Kilogram to Pound
              4. Pound to Kilogram
              5. Gram to Milligram
              6. Milligram to Gram
              7. Ton to Kilogram
              8. Kilogram to Ton
                                          '''))
                    
                    if user_inputZ==1:
                        a=float(input("enter the value "))
                        result=self.kg_to_g(a)
                        print(result)

                    elif user_inputZ==2:
                        a=float(input("enter the value "))
                        result=self.g_to_kg(a)
                        print(result)

                    elif user_inputZ==3:
                        a=float(input("enter the value "))
                        result=self.kg_to_pound(a)
                        print(result)

                    elif user_inputZ==4:
                        a=float(input("enter the value "))
                        result=self.pound_to_kg(a)
                        print(result)

                    elif user_inputZ==5:
                        a=float(input("enter the value "))
                        result=self.g_to_mg(a)
                        print(result)

                    elif user_inputZ==6:
                        a=float(input("enter the value "))
                        result=self.mg_to_g(a)
                        print(result)

                    elif user_inputZ==7:
                        a=float(input("enter the value "))
                        result=self.ton_to_kg(a)
                        print(result)

                    elif user_inputZ==8:
                        a=float(input("enter the value "))
                        result=self.kg_to_ton(a)
                        print(result)

                    else:
                        print("INVALID INPUT")

            elif self.user_input==5:
                user_input6=int(input('''
              What operation do you want to perform
                1. BMI
                2. Age Calculator
                                      '''))
                
                if user_input6==1:
                    a=float(input("enter the weight (in kg) "))
                    b=float(input("enter the height (in metres) "))
                    result=self.bmi(a,b)
                    print(result)

                elif user_input6==2:
                    print("enter DOB in YYYY format")
                    a=int(input("enter the DOB year "))
                    b=int(input("enter current year "))
                    result=self.age_calculator(a,b)
                    print("your age is " ,result, "years")
                
            elif self.user_input==6:
                print("Thanks for using calculator ")
                break
            
            else:
                print("INVALID INPUT ")

    def addition(self,n1,n2):
        total=n1+n2
        return total
    
    def subtraction(self,n1,n2):
        total=n1-n2
        return total
    
    def multiplication(self,n1,n2):
        total=n1*n2
        return total
    
    def division(self,n1,n2):
        total=n1/n2
        return total
    
    def square(self,n):
        result=n**2
        return result
    
    def squareroot(self,n):
        result=n**0.5
        return result
    
    def power(self,n1,n2):
        result=n1**n2
        return result
    
    def factorial(self,n):
        product=1
        for i in range(1,n+1):
            product=product*i
        return product
    
    def percentage(self,n1,n2):
        result=(n2/n1)*100
        return result
    
    def gst(self,n1,n2):
        result=n1+(n2/100)*n1
        return result
    
    def discount(self,n1,n2):
        discount_amount=n1-(n2/100)*n1
        amount_after_discount=n1-discount_amount
        return discount_amount,amount_after_discount
    
    def degree_to_fah(self,n):
        value=1.8*n+32
        return value
    
    def age_calculator(self,n1,n2):
       years=n2-n1
       return years
    
    def fah_to_degree(self,n):
        value=((n-32)*5)/9
        return value 

    def degree_to_kelv(self,n):
        value=n+273.15
        return value

    def kelv_to_degree(self,n):
        value=n-273.15
        return value      

    def m_to_km(self,n):
        value=n/1000
        return value

    def km_to_m(self,n):
        value=n*1000
        return value

    def cm_to_m(self,n):
        value=n/100
        return value

    def m_to_cm(self,n):
        value=n*100
        return value

    def cm_to_mm(self,n):
        value=n*10
        return value

    def mm_to_cm(self,n):
        value=n/10
        return value

    def inch_to_cm(self,n):
        value=n*2.54
        return value

    def foot_to_m(self,n):
        value = n/3.281
        return value 
    
    def kg_to_g(self,n):
        value=n*1000
        return value
    
    def g_to_kg(self,n):
        value=n/1000
        return value
    
    def kg_to_pound(self,n):
        value=n*2.205
        return value
    
    def pound_to_kg(self,n):
        value=n/2.205
        return value
    
    def g_to_mg(self,n):
        value=n*1000
        return value
    
    def mg_to_g(self,n):
        value=n/1000
        return value
    
    def ton_to_kg(self,n):
        value=n*1000
        return value
    
    def kg_to_ton(self,n):
        value=n/1000
        return value
    
    def bmi(self,n1,n2):
        value=n1/(n2**2)
        return value

obj=Calculator()
obj.menu()