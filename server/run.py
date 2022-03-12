import time
from urllib import request
from flask import Flask
from flask_cors import CORS
import loadData

#First load of possible trials to do
trialsList = loadData.load_init()
print(trialsList[0].toString())

app = Flask(__name__,  static_url_path='')
CORS(app)

devicesState = {1:False, 2:False, 3:False}

@app.route("/time")
def main_page():
    return {'time': time.time()}

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route("/device/<int:id>", methods=['PUT'])
def updateDeviceState(id:int):
    devicesState[id] = not devicesState[id]
    return {'state':devicesState[id]}

@app.route("/device/<int:id>", methods=['GET'])
def getDeviceState(id:int):
    return {'state':devicesState[id]}


if __name__ == '__main__':
    app.run(host='0.0.0.0')