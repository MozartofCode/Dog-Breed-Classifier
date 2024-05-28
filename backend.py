# @Author: Bertan Berker
# Using Flask Backend Framework in python,
# And a pretrained ML model, I am predicting the breed of your favorite pet (dog picture)
# And rendering information about your best friend!

import requests
from flask import redirect, request, send_from_directory, url_for
from flask import Flask, jsonify
from flask_cors import CORS
from classifier import get_breed
import json
from flask import render_template
import os

# API key for dog breed information from API ninjas
API_KEY = ""
UPLOAD_FOLDER = "uploads"

# Creating a Flask app
app = Flask(__name__)
CORS(app)


# This is useful for making sure that the frontend is getting the uploaded image
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(os.path.join(app.root_path, UPLOAD_FOLDER), filename)


# This function classifies the dog given the picture
# It takes the image file and uses the pretrained model to make the prediction
# And then calls the other functions to get and render information about that specific breed
@app.route('/api/classify', methods=['POST'])
def classify():
    print("Classify called...")
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['image']
    
    # Save the uploaded file
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Call the function from classify.py to classify the image
    result = get_breed(file)
    dog_info = get_information(result)    
    return redirect(url_for('render_information', dog_info=json.dumps(dog_info), image_url=f'uploads/{file.filename}'))


# Renders the information of the dog breed
@app.route('/info', methods=['GET'])
def render_information():
    dog_info = json.loads(request.args.get('dog_info'))
    image_url = request.args.get('image_url')
    return render_template('info.html', dog_info=dog_info, image_url=image_url)


# This is the function that makes the API call based on the name of the breed
# to get the information about that breed
# :param breed: Name of the dog breed based on the model's prediction
# :return: The info about the dog
def get_information(breed):

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