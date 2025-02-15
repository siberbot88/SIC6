from flask import Flask,jsonify,request
app = Flask(__name__)

list_temporary = []

@app.route('/sensor_farm', methods = ['POST'])
def simpan_data_sensorfarm ():
    if request.method == 'POST':
        body = request.get_json()
        temperature = body['temperature']
        humidity = body['humidity']
        timestamp = body['timestamp']
        
        average_data_sensor = (temperature + humidity)/2
        
        list_temporary.append({
            "temperature":temperature,
            "\nhumidity":humidity,
            "\ntimestamp":timestamp,
            "\nAverage":average_data_sensor
        })
        print("Current Database: ",list_temporary)
        return {
            "message":"Hello, I have your request",
            "average current": average_data_sensor
        }
    elif not request.method:
        return {
            "message":"request kamu gagal, mohon maaf"
        }

if __name__ == '__main__':
    app.run(port=5000,debug=True)