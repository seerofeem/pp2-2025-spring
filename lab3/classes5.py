class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Received {amount} units. New balance: {self.balance} units")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount} units. New balance: {self.balance} units")
            else:
                print("Insufficient amount")
        else:
            print("Withdrawal amount must be positive.")

    def __str__(self):
        return f"Owner: {self.owner}. Balance: {self.balance} units"

account = BankAccount("Arsen Bekeshov", 100)
print(account)
account.deposit(50) 
account.deposit(-10)  
account.withdraw(20) 
account.withdraw(200)
account.withdraw(-10)
print(account)  