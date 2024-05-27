# @Author: Bertan Berker
# Using Flask Backend Framework in python
#
#
#

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


# Create a Flask app
app = Flask(__name__)
CORS(app)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(os.path.join(app.root_path, UPLOAD_FOLDER), filename)


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

@app.route('/info', methods=['GET'])
def render_information():
    dog_info = json.loads(request.args.get('dog_info'))
    image_url = request.args.get('image_url')
    return render_template('info.html', dog_info=dog_info, image_url=image_url)


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