from flask import Flask, jsonify, request

app = Flask(__name__)

############################ PYMONGO SECTION ###########################
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://siberbot88:IQodF83Su0n4gFq5d@cluster-siberbot88.sw4in.mongodb.net/?retryWrites=true&w=majority&appName=Cluster-Siberbot88"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# database
db = client['MyDatabase']
my_collection = db['SensorData']

def store_data(data):
    result = my_collection.insert_one(data)
    print(result.inserted_id)
    return result.inserted_id

def get_data():
    get_result = my_collection.find()
    return get_result

########################################################################

@app.route('/', methods=['GET'])
def simpan():
    if request.method == 'GET':
        return jsonify({
            "message":"halo selamat datang boy"
        })
    if not request.method == 'GET':
        return jsonify({
            "message":"Tidak bisa boy"
        })
        
        
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
            "message": f"Data berhasil disimpan dengan id {id}",
            "average_current": average_data
        })
    
    elif request.method == 'GET':
        data = get_data()
        if not data:
            return jsonify({"warning": "Data kosong"}), 200
        
        return jsonify(data)

@app.route('/sensor1/temperature/avg', methods=['GET'])
def get_avg_temperature():
    if not list_temporary:
        return jsonify({
            "message": "Tidak ada data suhu tersedia",
            "average_temperature": None
        }), 200

    total = sum(entry['temperature'] for entry in id)
    average_temp = total / len(id)
    
    return jsonify({
        "average_temperature": round(average_temp, 2)  # data dibulatkan
    })

if __name__ == '__main__':
    app.run(port=1859, debug=True)
