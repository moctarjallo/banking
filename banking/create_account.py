from .domain import Client, Account

from banking.api import Request

class CreateAccount:
    def __init__(self, Response: type):
        self.Response = Response

    def execute(self, request: Request):
        client = Client(request.data['firstname'], \
                        request.data['lastname'], \
                        request.data['address'])
        account = Account(client, request.data['balance'])
        response = account.to_dict()
        return self.Response(response)
