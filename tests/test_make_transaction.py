import unittest

from banking import MakeTransaction

import pythonapi as api

class TestMakeDepositTransaction(unittest.TestCase):
    def setUp(self):
        self.make_transaction = MakeTransaction()

    def test_simple(self):
        request = api.Request({
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
        del transaction['time']
        response = api.Response(transaction)
        self.assertEqual(response.data, {
            'action': 'deposit',
            'amount': 100,
            'client_name': 'moctar',
            'account_code': 5221,
            'old_balance': 400,
            'new_balance': 500,
        })

class TestMakeWithdrawTransaction(unittest.TestCase):
    def setUp(self):
        self.make_transaction = MakeTransaction()

    def test_simple(self):
        request = api.Request({
            'action': 'withdraw',
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
        del transaction['time']
        response = api.Response(transaction)
        self.assertEqual(response.data, {
            'action': 'withdraw',
            'amount': 100,
            'client_name': 'moctar',
            'account_code': 5221,
            'old_balance': 400,
            'new_balance': 300,
        })

if __name__ == '__main__':
    unittest.main()