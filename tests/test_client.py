import unittest
from ebank.domain import Client

class TestClient(unittest.TestCase):
    def test_to_dict(self):
        client = Client('moctar', 'diallo', 'medina')
        self.assertEqual(client.to_dict(), {
            'firstname': 'moctar',
            'lastname': 'diallo',
            'address': 'medina'
        })