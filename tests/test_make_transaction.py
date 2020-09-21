import unittest

from ebank import MakeTransaction

from ebank.api import Request, Response

class TestMakeTransaction(unittest.TestCase):
    def setUp(self):
        self.make_transaction = MakeTransaction(Response)

    def test_simple(self):
        request = Request({
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