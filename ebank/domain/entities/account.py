import random

from .client import Client

class Account:
    def __init__(self, client: Client, balance):
        self.client = client
        self.balance = balance
        self._code = random.randint(1, 10000)

    def get_code(self):
        return self._code
