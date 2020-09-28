from .domain import Client, Account

import pythonapi as api

class CreateAccount:

    def execute(self, request: api.Request):
        client = Client(request['firstname'], \
                        request['lastname'], \
                        request['address'])
        account = Account(client, request['balance'])
        return account.to_dict()