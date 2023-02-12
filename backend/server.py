from flask import Flask, jsonify
import os
import datetime 
import random 
import json


x = datetime.datetime.now()

# Init the flask app
app = Flask(__name__)

base_dir = os.path.dirname(os.path.abspath(__file__))
fhir_dir = os.path.join(base_dir, '..', 'fhir')
file_names = os.listdir(fhir_dir)

@app.route('/')
def get_file_names():

    base_dir = os.path.dirname(os.path.abspath(__file__))
    fhir_dir = os.path.join(base_dir, '..', 'fhir')
    file_names = os.listdir(fhir_dir)
    random_file = random.choice(file_names)

    file_path = os.path.join(fhir_dir, random_file)
    if os.path.exists(file_path):
        print("The file exists")
    else:
        print("The file does not exist")

    with open(file_path, 'r') as f:
        content = json.load(f)

    print(content["entry"][0]["resource"]["address"][0]["city"])
    return jsonify(content)




'''@app.route('/api/files', methods=['GET'])
def get_file_names():
    file_names = os.listdir('./fhir')
    return jsonify(file_names)'''

if __name__ == '__main__':
    app.run(debug=True)
    