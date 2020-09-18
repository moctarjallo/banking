class Client:
    def __init__(self, firstname, lastname, address):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address

    @classmethod
    def from_dict(cls, data):
        return Client(data['firstname'],
                      data['lastname'],
                      data['address'])

    def to_dict(self):
        return {
            'firstname': self.firstname,
            'lastname': self.lastname,
            'address': self.address
        }