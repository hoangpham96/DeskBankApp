from datetime import datetime

class Customer:
    def __init__(self) -> None:
        self.name = input("Create Accounts for Customer: ")
        self.accounts = {}
        self.accounts["Savings"] = Account("Savings")
        self.accounts["Loan"] = Account("Loan")

    def readAmt(self):
        pass

    def verify(self, customerName):
        if self.name == customerName:
            self.menu()

    def lookup(self):
        pass

    def deposit(self):
        amount = float(input("Amount to deposit: $"))
        self.accounts["Savings"].deposit(amount)

    def withdraw(self):
        amount = float(input("Amount to withdraw: $"))
        self.accounts["Savings"].withdraw(amount) 
    
    def transfer(self):
        amount = float(input("Amount to transfer: $"))
        self.accounts["Savings"].transfer(self.accounts["Loan"],amount)

    def showBankAccounts(self):
        print(f"{self.name} bank statement {datetime.now()}")
        for key, account in self.accounts.items():
            account.showBalance()

    def toString(self):
        print(f"{self.name}\t\t--> Savings account has ${self.accounts['Savings'].balance:.2f}\t|Loan account has ${self.accounts['Loan'].balance:.2f}")

    def menu(self):
        print(f"Tom Banking Menu: {datetime.now()}")
        cmd = ''
        while cmd != 'x':
            prompt = "Customer menu(d/w/t/s/x): "
            cmd = input(prompt)
            match cmd.lower():
                case 'd':
                    self.deposit()
                case 'w':
                    self.withdraw()
                case 't':
                    self.transfer()
                case 's':
                    self.showBankAccounts()
                case 'x':
                    break
                case _:
                    print("Invalid Command. Please try again!")

class Account:
    def __init__(self, type) -> None:
        self.type = type
        self.balance = float(input(f"Enter {type} account balance: $"))
    
    def readBalance(self):
        pass

    def matchType(self):
        pass

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance += -amount
    
    def showBalance(self):
        print(f"{self.type} balance: ${self.balance}")
        
    def transfer(self, toAccount, amount):
        self.withdraw(amount)
        toAccount.deposit(amount)

class Bank:
    def __init__(self,admin):
        self.admin = admin
        self.customers = [Customer() for i in range(3)]
        self.menu()

    def login(self):
        name = input("Name: ")
        for customer in self.customers:
            customer.verify(name)

    def showCustomers(self):
        for customer in self.customers:
            customer.toString()

    def menu(self):
        print(f"Bank Menu: {datetime.now()}")
        cmd = ''
        while cmd != 'x':
            prompt = "Customer menu(L/V/X): "
            cmd = input(prompt)
            match cmd.lower():
                case 'l':
                    self.login()
                case 'v':
                    self.showCustomers()
                case 'x':
                    break
                case _:
                    print("Invalid Command. Please try again!")

if __name__ == '__main__':
    bank = Bank('Admin')