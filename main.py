from flask import Flask, jsonify


app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify(
        resp = "hello"
    )

@app.route('/greet', defaults={'name': 'Programmer'})
@app.route('/greet/<name>')
def greet(name):
    return jsonify(
        name=name
    )