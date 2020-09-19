from .entities import Client, Account

from .request import CreateAccountRequest

class CreateAccount:
    def __init__(self, Response: type):
        self.Response = Response

    def execute(self, request: CreateAccountRequest):
        client = Client(request.data['firstname'], \
                        request.data['lastname'], \
                        request.data['address'])
        account = Account(client, request.data['balance'])
        response = account.to_dict()
        return self.Response(response)
