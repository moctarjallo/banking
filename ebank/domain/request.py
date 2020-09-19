class Request:
    def __init__(self, response):
        self.response = response

    @property
    def data(self):
        return self.response


class CreateAccountRequest(Request):
    pass

class TransactionRequest(Request):
    pass