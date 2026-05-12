class Calculator:

    def __init__(self):
        self.history=[]

    def menu(self):
        while True:
            print("="*40)
            print("      WELCOME TO SMART CALCULATOR")
            print("="*40)
            self.user_input=input('''
              Select which calculator do you want
              1. Basic Calculator
              2. Scientific calculator
              3. Finance Calculator
              4. Unit Converter
              5. Health Calculator
                Enter your choice
              ''')
            if self.user_input==1:
                user_input2=input('''
              What operation do you want to perform
                1. Addition
                2. subtraction
                3. Multiply
                4. Division                  
                                  ''')
obj=Calculator()
print(obj.menu())