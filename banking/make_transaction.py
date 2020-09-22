import pythonapi as api

from .domain import Client, Account

class MakeTransaction:

    def execute(self, request: api.Request):
        client = Client.from_dict(request.data['account']['client'])
        account = Account(client, request.data['account']['balance'], \
                                  request.data['account']['code'])
        if request.data['action'] == 'deposit':
            trans = account.deposit(request.data['amount'])
        elif request.data['action'] == 'withdraw':
            trans = account.withdraw(request.data['amount'])
        return trans.to_dict()