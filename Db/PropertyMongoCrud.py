from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from Model.Property import Property

class PropertyCrud:
    def _init_(self, mongo):
        self.mongo = mongo
        self.properties = {}  # Optional: Keep for in-memory operations

    def create_property(self, data):
        house_id = self.mongo.db.properties.insert_one(data).inserted_id
        return str(house_id)

    def get_property(self, house_id):
        house = self.mongo.db.properties.find_one({'_id': ObjectId(house_id)})
        if house:
            house['_id'] = str(house['_id'])
            return house
        return None

    def update_property(self, house_id, data):
        result = self.mongo.db.properties.update_one({'_id': ObjectId(house_id)}, {'$set': data})
        return result.matched_count > 0

    def delete_property(self, house_id):
        result = self.mongo.db.properties.delete_one({'_id': ObjectId(house_id)})
        return result.deleted_count > 0