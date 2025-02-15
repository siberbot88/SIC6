from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def entry_point():
    return jsonify(message='hello world')

list_temp = []
@app.route('/sensor1',methods = ['POST'])
def simpan_data_sensor():
    if request.method == 'POST':
        body = request.get_json()
        temperature = body['temperature']
        humidity = body['humidity']
        timestamp = body['timestamp']
        resul_mean = (temperature + humidity)/2
        
        list_temp.append({
            "temperature":temperature,
            "humidity":humidity,
            "timestamp":timestamp,
            "result":resul_mean
        })
        print('cureent database: ',list_temp)
        # params = request.args.get('username')
        return {
            "message":"hello, I have processed you request",
            "Avg.":resul_mean
        }
    elif request.method == 'GET':
        return jsonify(message='Ambil saja semuanya kocak')

if __name__ == '__main__':
    app.run(port=5050,debug=True)

print('cureent database: ',list_temp)
    