#banking application code using OOP
class Atm:
    def __init__(self):
        self.pin=''
        self.balance=0
        self.menu()

    def menu(self):
        while True:

         self.user_input = input("""
        Hi How Can I Help You!!
        1. Press 1 to create pin
        2. Press 2 to change pin 
        3. Press 3 to check balance
        4. Press 4 to withdrawal
        5. Anything else to exit  
                                
    Enter your choice  """) 
         if self.user_input=='1': 
            self.create_pin()    #code for create pin
         elif self.user_input=='2':
            self.change_pin()    #code for change pin
         elif self.user_input=='3':
            self.check_balance() # code for check balance
         elif self.user_input=='4':
            self.withdrawal()      # code for withdrawl
         elif self.user_input=='5':   # code for exit
             print("Thank you for using ATM !!")
             break
         else:                         #anything without these numbers are invalid 
            print("Invalid choice")          
        
    def create_pin(self):
        user_pin=input('enter your pin ')
        self.pin=user_pin
        user_balance=int (input('enter your balance '))
        self.balance=user_balance
        print('pin created successfully')

    def change_pin(self):
        old_pin = input('enter your old pin ')

        if old_pin==self.pin:
          #let change the pin
          new_pin=input('enter new pin ')
          self.pin=new_pin
          print('pin change successfully ')
         
        else:
            print("your pin doesn't match with your old pin")  

    def check_balance(self):
        pin=input('enter your pin ')
        if pin==self.pin:
            print('Your Balance is',self.balance)
        else:
            print('Your Pin is Incorrect')

    def withdrawal(self):
        pin=input('enter your pin ')
        if pin==self.pin:
           amount=int(input('enter amount '))
           if amount<=self.balance:
               print('Transaction Successful')
               if amount<=self.balance:
                   new_balance=self.balance-amount
                   self.balance=new_balance
                   print('Your current balance is',self.balance)
                   
               else:
                   print('Your Balance is',self.balance)

           else:
               print('insufficient balance')
                   
        else:
            print('Incorrect Pin')

obj=Atm()