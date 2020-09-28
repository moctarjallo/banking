import pythonapi as api

from .domain import Client, Account

class MakeTransaction:

    def execute(self, request: api.Request):
        client = Client.from_dict(request['account']['client'])
        account = Account(client, request['account']['balance'], \
                                  request['account']['code'])
        if request['action'] == 'deposit':
            trans = account.deposit(request['amount'])
        elif request['action'] == 'withdraw':
            trans = account.withdraw(request['amount'])
        return trans.to_dict()