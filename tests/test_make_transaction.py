import unittest

from ebank.domain import MakeTransaction
from ebank.domain.agents import Agent

class TestMakeTransaction(unittest.TestCase):
    def setUp(self):
        self.agent = Agent()
        self.make_transaction = MakeTransaction(self.agent)

    def test_simple(self):
        request = {
            'action': 'deposit',
            'account': {
                'client': {
                    'firstname': 'moctar',
                    'lastname': 'diallo',
                    'address': 'medina'
                },
                'balance': 400,
                'code': 5221
            },
            'amount': 100
        }

        transaction = self.make_transaction.execute(request)
        self.assertEqual(transaction, {
            'action': 'deposit',
            'amount': 100,
            'client_name': 'moctar',
            'account_code': 5221,
            'old_balance': 400,
            'new_balance': 500,
        })