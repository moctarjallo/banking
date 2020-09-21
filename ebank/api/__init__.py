from .request import ParagraphRequest
from .response import ParagraphResponse

class Request:
    def __init__(self, request):
        self.data = self.parse(request)

    def parse(self, request):
        return ParagraphRequest(request).data

class Response:
    def __init__(self, request):
        self.data = self.parse(request)

    def parse(self, request):
        return ParagraphResponse(request).data