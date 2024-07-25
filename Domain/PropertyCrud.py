from Model.Property import Property


class PropertyCrud:
    def __init__(self):
        self.properties = {}

    def create_property(self, property_id, name, description, address, owner, city, price):
        if property_id in self.properties:
            return "House already exists"
        self.properties[property_id] = Property(name, description, address, owner, city, price)
        return "House created successfully"

    def get_property(self, house_id):
        house = self.properties.get(house_id)
        if not house:
            return "House not found"
        return house.to_dict()

    def update_property(self, house_id, name=None, description=None, address=None, owner=None, city=None, price=None):
        house = self.properties.get(house_id)
        if not house:
            return "House not found"
        if name:
            house.name = name
        if description:
            house.description = description
        if address:
            house.address = address
        if owner:
            house.owner = owner
        if city:
            house.city = city
        if price is not None:
            house.price = price
        return "House updated successfully"

    def delete_property(self, house_id):
        if house_id not in self.properties:
            return "Property not found"
        del self.properties[house_id]
        return "property deleted successfully"