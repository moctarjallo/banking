class Response:
    def __init__(self, response):
        self.data = self.parse(response)

    def parse(self, response):
        return response