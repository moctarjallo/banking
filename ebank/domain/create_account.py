from .entities import Client, Account

from .agents import ClientPresenter
from .request import CreateAccountRequest

class CreateAccount:
    def __init__(self, agent: ClientPresenter):
        self.agent = agent

    def execute(self, request: CreateAccountRequest):
        client = Client(request.data['firstname'], \
                        request.data['lastname'], \
                        request.data['address'])
        account = Account(client, request.data['balance'])
        response = {}
        response.update(request.data)
        response['code'] = account.get_code()
        return self.agent.present(response)
