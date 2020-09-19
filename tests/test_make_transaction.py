import unittest

from ebank.domain import MakeTransaction

from ebank.domain.request import MakeTransactionRequest
from ebank.domain.response import TransactionResponse

class TestMakeTransaction(unittest.TestCase):
    def setUp(self):
        self.make_transaction = MakeTransaction(TransactionResponse)

    def test_simple(self):
        request = MakeTransactionRequest({
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
        })

        transaction = self.make_transaction.execute(request)
        self.assertEqual(transaction.data, {
            'action': 'deposit',
            'amount': 100,
            'client_name': 'moctar',
            'account_code': 5221,
            'old_balance': 400,
            'new_balance': 500,
        })