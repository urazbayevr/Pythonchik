class BankAccount:

    kredit = 30

    def __init__(self, name):
        self.owner = name
        self.balance = 0.0

    def __repr__(self):
        return f"{self.owner} {self.balance}"

    def getBalance(self):
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.owner,self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.owner,self.balance

bank = BankAccount("Rama")
print(bank)
print(bank.deposit(50))
print(bank.getBalance())
print(bank.withdraw(30))
print(bank.getBalance())
