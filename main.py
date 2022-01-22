from crypt import methods
from json.tool import main
from flask import Flask, jsonify, request
from models.sensor import Sensor

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify(
        hello = "World"
    )

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
            "city": sensor.city
        }
    return jsonify(resp)

@app.route("/sensors/<uuid>")
def get_sensor_by_uuid(uuid):
    sensor = Sensor.get_sensor_by_uuid(uuid)
    
    if sensor:
        return jsonify({ 
            "uuid": sensor.uuid,
            "country": sensor.country,
            "city": sensor.city   
        })
    else:
        return jsonify({})