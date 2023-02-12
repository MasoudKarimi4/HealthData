from flask import Flask, jsonify
import os
import datetime 
import random 
import json
from flask_cors import CORS


x = datetime.datetime.now()

# Init the flask app
app = Flask(__name__)
CORS(app)

base_dir = os.path.dirname(os.path.abspath(__file__))
fhir_dir = os.path.join(base_dir, '..', 'fhir')
file_names = os.listdir(fhir_dir)

def getWorkingFile():


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

    
@app.route('/route', methods=['GET'])
def route():
    print("It worked")

    

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

    #print(content["entry"][0]["resource"]["address"][0]["city"])
    try: 
        clinical = (content["entry"][4]["resource"]['code']["text"])
        print(clinical)
        if clinical != 'Body Height':
            return jsonify(clinical)
        else:
            return jsonify("Diabetes")
    except KeyError:
        print("Aspergers")


        return jsonify("Common Flu")
    return jsonify("Indeterminate")





if __name__ == '__main__':
    app.run(debug=True)
    