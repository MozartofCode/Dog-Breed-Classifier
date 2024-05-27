# @Author: Bertan Berker
# Using Flask Backend Framework in python
#
#
#

import requests
from flask import request
from flask import Flask, jsonify
from flask_cors import CORS
import base64
from pymongo import MongoClient
from pymongo.mongo_client import MongoClient
import certifi

# Create a Flask app
app = Flask(__name__)
CORS(app)


@app.route('/api/classify', methods=['GET'])
def classify():
    return


@app.route('/api/getInformation', methods=['GET'])
def get_information():
    return

