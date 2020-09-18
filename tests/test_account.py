import unittest

from ebank.domain.entities import Account, Client

class TestGetCode(unittest.TestCase):
    def test_general(self):
        client = Client('moctar', 'diallo', 'medina')
        account = Account(client, 400)
        self.assertLess(account.get_code(), 10000)
        self.assertGreaterEqual(account.get_code(), 1)

if __name__ == '__main__':
    unittest.main()