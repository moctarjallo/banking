from datetime import datetime as date

class Transaction:
    def __init__(self, action, amount, client_name, account_code, old_balance, new_balance):
        self.client_name = client_name
        self.account_code = account_code
        self.action = action
        self.amount = amount
        self.old_balance = old_balance
        self.new_balance = new_balance
        self.time = date.now().ctime()

    def to_dict(self):
        return self.__dict__

    class Error(Exception):
        pass
