class BankAccount:
    def __init__(self, int_rate= 0, balance= 0):
        self.interest = int_rate/100
        self.account_balance = balance
    def deposit(self, amount):
        self.account_balance += amount
        return self
    def withdraw(self, amount):
        if self.account_balance > 0:
            self.account_balance -= amount
        else:
            print (f"Insufficient funds, charging a $5 fee")
            self.account_balance -= (amount + 5)
        return self
    def display_account_info(self):
        print(self.account_balance)
        return self
    def yield_interest(self):
        if self.account_balance > 0:
            self.int_balance = self.interest * self.account_balance + self.account_balance
        return self

user1 = BankAccount(balance = 150)
user2 = BankAccount(int_rate= 3, balance = 200)

user1.deposit(100).deposit(75).deposit(215).withdraw(85).yield_interest().display_account_info()
user2.deposit(185).deposit(315).withdraw(75).withdraw(110).withdraw(415).withdraw(60).yield_interest().display_account_info()