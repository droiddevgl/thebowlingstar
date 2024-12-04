from Account import Account

class CheckingAccount(Account):
    def __init__(self, name_of_account, amount):
        Account.__init__(self, name_of_account, amount)
        self.type_of_account = 'Checking'

    def getAccountType(self):
        return self.type_of_account

    def getStats(self):
        return f'Name: {self.name_of_account}\nType of Account: {self.type_of_account}\nBalance: {self.amount}'
