import unittest

from ebank.domain.entities import Account, Client

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.client = Client('moctar', 'diallo', 'medina')
        self.account = Account(self.client, 400)

    def test_init(self):
        account = Account(self.client, 400)
        self.assertLess(account.get_code(), 10000)
        self.assertGreaterEqual(account.get_code(), 1)

    def test_init_with_code(self):
        account = Account(self.client, 400, code=4444)
        self.assertEqual(account.get_code(), 4444)

    def test_deposit(self):
        self.account.deposit(100)
        self.assertEqual(self.account.balance, 500)

    def test_withdraw(self):
        self.account.withdraw(200)
        self.assertEqual(self.account.balance, 200)

    def test_to_dict(self):
        d = self.account.to_dict()
        self.assertEqual(d,
            {
                'client': {
                    'firstname': 'moctar',
                    'lastname': 'diallo',
                    'address': 'medina'
                },
                'balance': 400,
            }
        )


if __name__ == '__main__':
    unittest.main()