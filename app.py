from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# Configure MongoDB
app.config["MONGO_URI"] = "mongodb+srv://cristiantorresf:7aoC1gQ5gZLaUlkC@cluster0.1ijuu.azure.mongodb.net/HOUSELYPYTHON?ssl=true&tlsAllowInvalidCertificates=true"
mongo = PyMongo(app)

@app.route("/hello", methods=['GET'])
def hello():
    print(":O >>>>>> request received")
    sum=1+5
    return f'HELLO THERE MY SERVER IS WORKING 🥳🥳🥳🥳🥳🥳 {sum}'

@app.route('/getAllProperties', methods=['GET'])
def get_all_properties():
    properties = mongo.db.properties.find()
    result = []
    for property in properties:
        property['_id'] = str(property['_id'])
        result.append(property)
    return jsonify(result), 200

@app.route('/createproperty', methods=['POST'])
def create_property():
    data = request.get_json()
    house_id = mongo.db.properties.insert_one(data).inserted_id
    return jsonify(str(house_id)), 201

@app.route('/getPropertyById/<id>', methods=['GET'])
def get_property(id):
    house = mongo.db.properties.find_one({'_id': ObjectId(id)})
    if house:
        house['_id'] = str(house['_id'])
        return jsonify(house), 200
    return jsonify({'error': 'House not found'}), 404

@app.route('/properties/<id>', methods=['PUT'])
def update_ho(id):
    data = request.get_json()
    result = mongo.db.properties.update_one({'_id': ObjectId(id)}, {'$set': data})
    if result.matched_count:
        return jsonify({'message': 'House updated successfully'}), 200
    return jsonify({'error': 'House not found'}), 404

@app.route('/properties/<id>', methods=['DELETE'])
def delete_house(id):
    result = mongo.db.properties.delete_one({'_id': ObjectId(id)})
    if result.deleted_count:
        return jsonify({'message': 'House deleted successfully'}), 200
    return jsonify({'error': 'House not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
