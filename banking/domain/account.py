import random

from .client import Client
from .transaction import Transaction

class Account:
    def __init__(self, client: Client, balance, code=None):
        self.client = client
        self.balance = balance
        if code:
            self._code = int(code)
        else:
            self._code = random.randint(1, 10000)

    def get_code(self):
        return self._code

    def deposit(self, amount):
        try:
            amount = float(amount)
        except TypeError:
            raise Transaction.Error(f"{amount} should be a number")
        old_balance = self.balance
        self.balance += amount
        return Transaction(self.deposit.__name__, amount, self.client.firstname, self.get_code(), old_balance, self.balance)

    def withdraw(self, amount):
        try:
            amount = float(amount)
        except TypeError:
            raise Transaction.Error(f"{amount} should be a number")
        if amount > self.balance:
            raise Transaction.Error(f"You don't have enough money in your account")
        old_balance = self.balance
        self.balance -= amount
        return Transaction(self.withdraw.__name__, amount, self.client.firstname, self.get_code(), old_balance, self.balance)

    def to_dict(self):
        return {
            "client": self.client.to_dict(),
            "balance": self.balance,
            "code": self._code
        }
