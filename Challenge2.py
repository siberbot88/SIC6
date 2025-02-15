from flask import Flask, jsonify, request
import database

app = Flask(__name__)

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://siberbot88:ykYIJkGZLpsL37Td@cluster-siberbot88.sw4in.mongodb.net/?retryWrites=true&w=majority&appName=Cluster-Siberbot88"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# kita bikin database
db = client['MyDatabase']
my_collection = db['SensorData']

def store_data(data):
    result = my_collection.insert_one(data)
    print(result.inserted_ids)
    return result.inserted_ids

def get_data():
    get_result = my_collection.find()
    return get_result

@app.route('/sensor_farm', methods=['POST', 'GET'])
def simpan_data_sensorfarm():
    if request.method == 'POST':
        body = request.get_json()
        temperature = body.get('temperature')
        humidity = body.get('humidity')
        timestamp = body.get('timestamp')

        average_data = (temperature + humidity) / 2
        
        data_final = {
            "temperature": temperature,
            "humidity": humidity,
            "timestamp": timestamp,
            "Average": average_data
        }
        
        id = store_data(data_final)
        return jsonify({
            "message": "Data berhasil disimpan dengan id {id}",
            "average_current": average_data
        })
    
    elif request.method == 'GET':
        return jsonify(get_data)

# @app.route('/sensor1/temperature/avg', methods=['GET'])
# def get_avg_temperature():
#     if not list_temporary:
#         return jsonify({
#             "message": "Tidak ada data suhu tersedia",
#             "average_temperature": None
#         }), 200

#     total = sum(entry['temperature'] for entry in id)
#     average_temp = total / len(id)
    
#     return jsonify({
#         "average_temperature": round(average_temp, 2)  # data dibulatkan
#     })

if __name__ == '__main__':
    app.run(port=5000, debug=True)