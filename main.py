from flask import Flask, request, jsonify
# import pymongo
from datetime import datetime
from pymongo.server_api import ServerApi
from flask_pymongo import PyMongo
import json, certifi

app = Flask(__name__)
app.config["SECRET_KEY"] = "4bd20b174ad0cf543619b769972825a3bc72aac8"
app.config['DEBUG'] = True
app.config['MONGO_URI'] = 'mongodb+srv://adminaccount:AGenericPassword@iotproject.4vkcamj.mongodb.net/iotproject?retryWrites=true&w=majority'
mongodb_client = PyMongo(app, tlsCAFile=certifi.where())
db = mongodb_client.db
# client = pymongo.MongoClient(
#         'mongodb+srv://adminaccount:AGenericPassword@iotproject.4vkcamj.mongodb.net/?retryWrites=true&w=majority')  # , server_api=ServerApi('1')
#     db = client.iotproject
#     records = db.records


# collection_name = mongo.db.collection_name


@app.route('/record/', methods=['GET'])
def activate():
    print(datetime.now())
    # print(pymongo.version)

    data = {
        "timestamp": datetime.now(),
        "temperature": 29.32,
        "humidity": 44.12,
        "motiondetected": True,
        "deviceid": 3
    }
    db.records.insert_one(data)
    # deviceid = -1
    # minute = datetime.utcnow().replace(second=0, microsecond=0)
    #
    # db.time_bucket.update_one(
    #     {'deviceId': deviceid, 'd': minute},
    #     {
    #         '$push': {'samples': data},
    #         '$inc': {'nsamples': 1}
    #     },
    #     upsert=True
    # )

    return jsonify({'data sent': True})


@app.route('/records/')
def get_all_records():
    documents = db.records.find({})
    for document in documents:
        print(document)
    return jsonify({'data retrieved': True})#, 404

@app.route('/records/device/<int:deviceid>')
def get_all_records_per_deviceid(deviceid):
    documents = db.records.find({"deviceid":deviceid})
    for document in documents:
        print(document)
    return jsonify({'data retrieved': True})#, 404

@app.route('/records/device/date')#<datetime:datetime>
def get_all_records_per_date():#datetime
    documents = db.records.find({"timestamp":})
    for document in documents:
        print(document)
    return jsonify({'data retrieved': True})#, 404

# @app.route('/receipts/<int:id>', methods=['PUT'])
# def update_receipt_by_id(id):
#     receipt = [receipt for receipt in data if receipt['id'] == id]
#     if len(receipt) == 0:
#         return {'message': f'The id {id} is not a valid receipt id'}, 404
#     if not request.json:
#         return {'message': f'the body of this request is empty'}, 400
#     if 'store' not in request.json:
#         return {'message': f'the store of this request is not valid'}, 400
#     if 'email' not in request.json :
#         return {'message': f'the email of this request is not valid'}, 400
#     if 'amount' in request.json is None:
#         return {'message': f'the amount of this request is not valid'}, 400
#     receipt[0]['store'] = request.json.get('store', receipt[0]['store'])
#     receipt[0]['email'] = request.json.get('email', receipt[0]['email'])
#     receipt[0]['amount'] = request.json.get('amount', receipt[0]['amount'])
#     return jsonify({'receipt': receipt[0]});



# if __name__ == '__main__':
#     print_hi('PyCharm')