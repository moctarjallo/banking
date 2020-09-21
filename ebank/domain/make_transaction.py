from ebank.api import Request, Response

from .entities import Client, Account

class MakeTransaction:
    def __init__(self, Response: type):
        self.Response = Response

    def execute(self, request: Request):
        client = Client.from_dict(request.data['account']['client'])
        account = Account(client, request.data['account']['balance'], \
                                  request.data['account']['code'])
        if request.data['action'] == 'deposit':
            trans = account.deposit(request.data['amount'])
        elif request.data['action'] == 'withdraw':
            trans = account.withdraw(request.data['amount'])
        response = self.Response(trans.to_dict())
        return response