from flask import Flask, jsonify, request

app = Flask(__name__)

list_temporary = [
    {"temperature": 25, "humidity": 60, "timestamp": "2023-10-10T12:00:00"},
    {"temperature": 26, "humidity": 58, "timestamp": "2023-10-10T12:05:00"},
    {"temperature": 24, "humidity": 65, "timestamp": "2023-10-10T12:10:00"}
]

@app.route('/sensor_farm', methods=['POST', 'GET'])
def simpan_data_sensorfarm():
    if request.method == 'POST':
        body = request.get_json()
        temperature = body.get('temperature')
        humidity = body.get('humidity')
        timestamp = body.get('timestamp')

        average_data = (temperature + humidity) / 2
        
        list_temporary.append({
            "temperature": temperature,
            "humidity": humidity,
            "timestamp": timestamp,
            "Average": average_data
        })
        
        return jsonify({
            "message": "Data berhasil disimpan",
            "average_current": average_data
        })
    
    elif request.method == 'GET':
        return jsonify(list_temporary)

@app.route('/sensor1/temperature/avg', methods=['GET'])
def get_avg_temperature():
    if not list_temporary:
        return jsonify({
            "message": "Tidak ada data suhu tersedia",
            "average_temperature": None
        }), 200

    total = sum(entry['temperature'] for entry in list_temporary)
    average_temp = total / len(list_temporary)
    
    return jsonify({
        "average_temperature": round(average_temp, 2)  # data dibulatkan
    })

if __name__ == '__main__':
    app.run(port=5000, debug=True)