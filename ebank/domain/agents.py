# Abstract classes implemented by technology-specific developers

class Controller:
    def process(self, data):
        return data

class Presenter:
    def present(self, data):
        return data

class Agent(Controller, Presenter):
    pass