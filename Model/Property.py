class Property:
    def __init__(self, name, description, address, owner, city, price):
        self.name = name
        self.description = description
        self.address = address
        self.owner = owner
        self.city = city
        self.price = price
    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'address': self.address,
            'owner': self.owner,
            'city': self.city,
            'price': self.price
        }
