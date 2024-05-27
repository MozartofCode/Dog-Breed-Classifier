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
import json
from flask import render_template


# API key for dog breed information from API ninjas
API_KEY = ""



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

    dog_info = get_information(result)
    
    if dog_info:
        return jsonify(dog_info)
    else:
        return jsonify({'error': 'Breed information not found'}), 404


@app.route('/info', methods=['GET'])
def render_information():    
    dog_info = request.args.to_dict()
    return render_template('info.html', dog_info=dog_info)




def get_information(breed):

    print("This is a " + breed)

    name_format = breed.split("_")
    
    name = ""

    for i in range(len(name_format)):

        name += name_format[i].lower()

        if i != (len(name_format) - 1):
            name += " "        

    api_url = 'https://api.api-ninjas.com/v1/dogs?name={}'.format(name)
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})

    if response.status_code == requests.codes.ok:

        dog_data = json.loads(response.text)
        return dog_data[0]

    else:
        print("Error:", response.status_code, response.text)
        return None


if __name__ == '__main__':
    app.run(debug=True)