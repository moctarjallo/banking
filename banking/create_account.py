from .domain import Client, Account

import pythonapi as api

class CreateAccount:

    def execute(self, request: api.Request):
        client = Client(request.data['firstname'], \
                        request.data['lastname'], \
                        request.data['address'])
        account = Account(client, request.data['balance'])
        return account.to_dict()