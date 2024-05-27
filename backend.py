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


from classifier import get_breed


# Create a Flask app
app = Flask(__name__)
CORS(app)


@app.route('/api/classify', methods=['POST'])
def classify():
    print("Classify called...")
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['image']
    
    # Call the function from classify.py to classify the image
    result = get_breed(file)

    return jsonify({'result': result})







@app.route('/api/getInformation', methods=['GET'])
def get_information():
    return


if __name__ == '__main__':
    app.run(debug=True)