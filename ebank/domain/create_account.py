from .entities import Client, Account

from .agents import Agent

class CreateAccount:
    def __init__(self, agent: Agent):
        self.agent = agent

    def execute(self, client_request):
        client = Client(client_request['firstname'], \
                        client_request['lastname'], \
                        client_request['address'])
        account = Account(client, client_request['balance'])
        response = {}
        response.update(client_request)
        response['code'] = account.get_code()
        return self.agent.present(response)
