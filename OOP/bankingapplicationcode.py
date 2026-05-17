# ATM Banking Application using OOP in Python

class Atm:

    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.history = []
        self.menu()

    def menu(self):

        while True:

            print("\n" + "=" * 45)
            print("        WELCOME TO ATM MACHINE")
            print("=" * 45)

            self.user_input = input('''
1. Create PIN
2. Change PIN
3. Check Balance
4. Deposit Money
5. Withdraw Money
6. Transaction History
7. Exit

Enter your choice: ''')

            if self.user_input == '1':
                self.create_pin()

            elif self.user_input == '2':
                self.change_pin()

            elif self.user_input == '3':
                self.check_balance()

            elif self.user_input == '4':
                self.deposit()

            elif self.user_input == '5':
                self.withdrawal()

            elif self.user_input == '6':
                self.transaction_history()

            elif self.user_input == '7':
                print("\nThank you for using ATM Machine !!")
                break

            else:
                print("\nInvalid Choice")

    # Create PIN
    def create_pin(self):

        if self.pin != "":
            print("\nPIN already created")
            return

        user_pin = input('Enter your new PIN: ')

        if len(user_pin) != 4 or not user_pin.isdigit():
            print("PIN must contain exactly 4 digits")
            return

        self.pin = user_pin

        user_balance = int(input('Enter your opening balance: '))

        if user_balance < 0:
            print("Balance cannot be negative")
            return

        self.balance = user_balance

        self.history.append(f"Account created with balance ₹{user_balance}")

        print('PIN created successfully')

    # Change PIN
    def change_pin(self):

        if self.pin == "":
            print("\nPlease create PIN first")
            return

        old_pin = input('Enter your old PIN: ')

        if old_pin == self.pin:

            new_pin = input('Enter new PIN: ')

            if len(new_pin) != 4 or not new_pin.isdigit():
                print("PIN must contain exactly 4 digits")
                return

            self.pin = new_pin

            self.history.append("PIN changed successfully")

            print('PIN changed successfully')

        else:
            print("Incorrect old PIN")

    # Check Balance
    def check_balance(self):

        if self.pin == "":
            print("\nPlease create PIN first")
            return

        pin = input('Enter your PIN: ')

        if pin == self.pin:
            print(f'Your Balance is ₹{self.balance}')

        else:
            print('Incorrect PIN')

    # Deposit Money
    def deposit(self):

        if self.pin == "":
            print("\nPlease create PIN first")
            return

        pin = input('Enter your PIN: ')

        if pin == self.pin:

            amount = int(input('Enter amount to deposit: ₹'))

            if amount <= 0:
                print("Amount must be greater than 0")
                return

            self.balance += amount

            self.history.append(f"Deposited ₹{amount}")

            print('Deposit Successful')
            print(f'Updated Balance is ₹{self.balance}')

        else:
            print('Incorrect PIN')

    # Withdraw Money
    def withdrawal(self):

        if self.pin == "":
            print("\nPlease create PIN first")
            return

        pin = input('Enter your PIN: ')

        if pin == self.pin:

            amount = int(input('Enter withdrawal amount: ₹'))

            if amount <= 0:
                print("Amount must be greater than 0")
                return

            if amount <= self.balance:

                self.balance -= amount

                self.history.append(f"Withdrawn ₹{amount}")

                print('Transaction Successful')
                print(f'Current Balance is ₹{self.balance}')

            else:
                print('Insufficient Balance')

        else:
            print('Incorrect PIN')

    # Transaction History
    def transaction_history(self):

        if len(self.history) == 0:
            print("\nNo transaction history available")

        else:
            print("\n========== TRANSACTION HISTORY ==========")

            for index, transaction in enumerate(self.history, start=1):
                print(f"{index}. {transaction}")

atm_machine = Atm()