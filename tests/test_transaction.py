import unittest

from banking.domain import Transaction

class TestTransaction(unittest.TestCase):
    def test_to_dict(self):
        trans = Transaction('deposit', 100, 'moctar', 5221, 300, 400)
        trans_dict = trans.to_dict()
        del trans_dict['time']
        self.assertEqual(trans_dict, {
            'action': 'deposit',
            'amount': 100,
            'client_name': 'moctar',
            'account_code': 5221,
            'old_balance': 300,
            'new_balance': 400
        })

if __name__ == '__main__':
    unittest.main()