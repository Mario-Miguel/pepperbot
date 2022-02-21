import time
from flask import Flask

app = Flask(__name__)

@app.route("/time")
def main_page():
    return {'time': time.time()}