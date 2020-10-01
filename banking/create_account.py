from .domain import Client, Account
class CreateAccount:

    def execute(self, request: {}):
        client = Client(request['firstname'], \
                        request['lastname'], \
                        request['address'])
        account = Account(client, request['balance'])
        return account.to_dict()