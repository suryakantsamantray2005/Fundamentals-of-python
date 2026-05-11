#Create a Python class called BankAccount which represents a bank account, 
# having as attributes: accountNumber (numeric type), name 
# (name of the account owner as string type), balance.
#Create a constructor with parameters: accountNumber, name, balance.
#Create a Deposit() method which manages the deposit actions.
#Create a Withdrawal() method which manages withdrawals actions.
#Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
#Create a display() method to display account details. Give the complete code for the BankAccount class.

class BankAccount:
    
    def __init__(self,account_number,name,balance):
        self.account_number=account_number
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        self.balance=self.balance+amount
        print('Deposited succesfully - ',amount)

    def withdrawal(self,amount1):
        if self.balance>=amount1:
           self.balance=self.balance-amount1
           print('Withdrawl amount of',amount1, 'successful')
        else:
            print('Insufficient Balance')

    def bank_fees(self):
        bank_fees=self.balance*0.05
        self.balance = self.balance - bank_fees
        print('the bank fees is',bank_fees)

    def display(self):
        print('Account Number :',self.account_number)
        print('Account Name :',self.name)
        print('Account balance :',self.balance)

acc1 = BankAccount(4456127234,'Suryakant',10000)
acc1.deposit(2000)
acc1.display()