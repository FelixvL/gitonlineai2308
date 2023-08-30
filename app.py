from flask import Flask
from flask_cors import CORS, cross_origin
import felixbestand

app = Flask(__name__)
cors = CORS(app)

@app.route("/")
def hello_world():

    return "<p>Hello, World!</p>"

@app.route("/tweede/<key>/<destad>")
def hello_world2(key,destad):

    return felixbestand.ditismijnfunctie(key,destad)