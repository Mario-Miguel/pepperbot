from urllib import request
from flask import Flask
from flask_cors import CORS
import loadData

#Load of possible trials to do
trialsList = loadData.load_init()
print(trialsList[0].toString())

app = Flask(__name__,  static_url_path='')
CORS(app)

devicesState = {1:False, 2:False, 3:False}


@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route("/device/<int:id>", methods=['PUT'])
def updateDeviceState(id:int):
    devicesState[id] = not devicesState[id]
    if(areDevicesReady()):
        startGrpcConnection()
    return {'state':devicesState[id]}


@app.route("/device/<int:id>", methods=['GET'])
def getDeviceState(id:int):
    return {'state':devicesState[id]}


def areDevicesReady():
    return devicesState[0] and devicesState[1] and devicesState[2]

def startGrpcConnection():
    return

if __name__ == '__main__':
    app.run(host='0.0.0.0')