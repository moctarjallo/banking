from .domain import Client, Account, Transaction

class MakeTransaction:

    def execute(self, request: {}):
        client = Client.from_dict(request['account']['client'])
        account = Account(client, request['account']['balance'], \
                                  request['account']['code'])
        if request['action'] in ['deposit', 'd']:
            trans = account.deposit(request['amount'])
        elif request['action'] in ['withdraw', 'w']:
            trans = account.withdraw(request['amount'])
        else:
            raise Transaction.Error(f"Action {request['action']} not recognized")
        return trans.to_dict()