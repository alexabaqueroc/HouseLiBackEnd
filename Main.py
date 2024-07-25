
from Domain import PropertyCrud

house_manager = PropertyCrud.PropertyCrud()
house_manager.create_property(
    1,
    "Casa Cajica",
    "Casa en conjunto cerrado ubicada en Cajica",
    "Km 1",
    "Gustavo Garcia",
    "Cajica",
    740000000)
dic = house_manager.get_property(1)
print(dic)