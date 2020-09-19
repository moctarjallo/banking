class Response:
    def __init__(self, request):
        self.request = request

    @property
    def data(self):
        return self.request


class AccountResponse(Response):
    pass

class TransactionResponse(Response):
    pass
