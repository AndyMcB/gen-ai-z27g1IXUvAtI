from flask import Flask, jsonify, request
from models.sensor import Sensor
from models.sensor_data import SensorData

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify(
        hello = "World"
    )

### Sensor Data Endpoints 

@app.route("/sensor_data/create", methods=["POST"])
def create_sensor_data():
    request_data = request.get_json()    
    try:
        sensor_data = SensorData(request_data["sensor_uuid"], request_data["temp"], request_data["humidity"], request_data["wind_speed"])
        result = sensor_data.save()
 
        if result["success"]:
            return jsonify(code=200, msg=result["msg"])
        else:
            return jsonify(code=500, msg=result["msg"])
    except KeyError:
        return jsonify(code = 400, msg = "Attribute key missing")

@app.route("/sensor_data/all")
def get_all_sensor_data():
    sensor_data = SensorData.get_all_sensor_data()
    resp = {}
    for sensor_datum in sensor_data:
        if sensor_datum.sensor_uuid not in resp.keys():
            resp[sensor_datum.sensor_uuid] = []

        resp[sensor_datum.sensor_uuid].append({
            "sensor_uuid": sensor_datum.sensor_uuid,
            "temp": sensor_datum.temp,
            "humidity": sensor_datum.humidity,
            "wind_speed": sensor_datum.wind_speed,
            "created_at": sensor_datum.created_at
        })
    return jsonify(resp)

@app.route("/sensor_data/<sensor_uuid>")
def get_sensor_data_by_sensor_uuid(sensor_uuid):
    sensor_data = SensorData.get_sensor_data_by_sensor_uuid(sensor_uuid)
    
    resp = {}
    for sensor_datum in sensor_data:
        if sensor_datum.sensor_uuid not in resp.keys():
            resp[sensor_datum.sensor_uuid] = []

        resp[sensor_datum.sensor_uuid].append({
            "sensor_uuid": sensor_datum.sensor_uuid,
            "temp": sensor_datum.temp,
            "humidity": sensor_datum.humidity,
            "wind_speed": sensor_datum.wind_speed,
            "created_at": sensor_datum.created_at
        })
    return jsonify(resp)

### Sensor Endpoints 
@app.route("/sensors/create", methods=["POST"])
def create_sensor():
    request_data = request.get_json()
    try:
        sensor = Sensor(request_data["uuid"], request_data["country"], request_data["city"])
        result = sensor.save()
        print(result)
 
        if result["success"]:
            return jsonify(code=200, msg=result["msg"])
        else:
            return jsonify(code=500, msg=result["msg"])
    except KeyError:
        return jsonify(code = 400, msg = "Attribute key missing")

@app.route("/sensors/all")
def get_all_sensors():
    sensors = Sensor.get_all_sensors()
    resp = {}
    for sensor in sensors:
        resp[sensor.uuid] = {
            "uuid": sensor.uuid,
            "country": sensor.country,
            "city": sensor.city,
            "created_at": sensor.created_at
        }
    return jsonify(resp)

@app.route("/sensors/<uuid>")
def get_sensor_by_uuid(uuid):
    sensor = Sensor.get_sensor_by_uuid(uuid)
    
    if sensor:
        return jsonify({ 
            "uuid": sensor.uuid,
            "country": sensor.country,
            "city": sensor.city,
            "created_at": sensor.created_at   
        })
    else:
        return jsonify({})