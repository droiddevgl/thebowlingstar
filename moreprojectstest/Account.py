class Account:
    def __init__(self, name_of_account, amount):
        self.name_of_account = name_of_account
        self.amount = amount

    def setAmount(self, amount):
        self.amount = amount

    def getAmount(self):
        return self.amount

    def deposit(self, amount):
        self.amount += amount

    def withdraw(self,amount):
        if self.amount == 0:
            return

        self.amount -= amount