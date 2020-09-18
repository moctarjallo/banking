class Client:
    def __init__(self, firstname, lastname, address):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address

    def from_dict(self, data):
        return Client(data['firstname'],
                      data['lastname'],
                      data['address'])