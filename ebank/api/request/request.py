class Request:
    def __init__(self, request):
        self.data = self.parse(request)

    def parse(self, request):
        return request
