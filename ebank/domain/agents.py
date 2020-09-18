# Abstract classes implemented by technology-specific developers

class Controller:
    def process(self, data):
        return data

class Presenter:
    def present(self, data):
        if isinstance(data, dict):
            return data
        else:
            return data.to_dict()

class Agent(Controller, Presenter):
    pass

class ClientPresenter(Presenter):
    def present(self, data):
        return data

class TransactionAgent(Agent):
    pass