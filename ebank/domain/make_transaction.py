from .agents import TransactionAgent

from .request import TransactionRequest

from .entities import Client, Account

class MakeTransaction:
    def __init__(self, agent: TransactionAgent):
        self.agent = agent

    def execute(self, request: TransactionRequest):
        client = Client.from_dict(request.data['account']['client'])
        account = Account(client, request.data['account']['balance'], \
                                  request.data['account']['code'])
        if request.data['action'] == 'deposit':
            trans = account.deposit(request.data['amount'])
        elif request.data['action'] == 'withdraw':
            trans = account.withdraw(request.data['amount'])
        response = self.agent.present(trans)
        return response