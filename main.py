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

@app.route("/sensor/create", methods=["POST"])
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