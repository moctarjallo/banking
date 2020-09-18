from .agents import TransactionAgent

from .entities import Client, Account

class MakeTransaction:
    def __init__(self, agent: TransactionAgent):
        self.agent = agent

    def execute(self, request):
        client = Client.from_dict(request['account']['client'])
        account = Account(client, request['account']['balance'], request['account']['code'])
        if request['action'] == 'deposit':
            trans = account.deposit(request['amount'])
        elif request['action'] == 'withdraw':
            trans = account.withdraw(request['amount'])
        response = self.agent.present(trans)
        return response