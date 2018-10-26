from flask import Flask
import fetch_data as fd
app = Flask(__name__)

@app.route("/")
def hello():
    return fd.alert()
