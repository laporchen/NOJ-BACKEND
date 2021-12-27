import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS
import traceback
import json

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

CORS(app, resources={r'/*': {'origins': '*'}})
data = {}
dataLocation = "./data"
dataName = "TASKS.json"
@app.route('/savetoserver', methods=['POST'])
def savetoserver():
  global data
  if request.method == 'POST':
    try:
        post_data = request.get_json()
        f = open(dataLocation + "/" + dataName,"w+")
        
        data = json.loads(post_data.get("info"))
        message = {'status': 'success'}
        try:
            jsonFile = json.dumps(data)
            f.write(jsonFile)
            f.close()
        except Exception:
            print("dataFile cannot be written. Please check the system.")
            message = {'status': 'fail'}
        
    except Exception as e:
        traceback.print_exc()
        return jsonify({'status': 'fail'})
    else:
        return jsonify(message)
@app.route('/get_data', methods=['GET'])
def get_data():
  global data
  if request.method == 'GET':
    try:
        f = open(dataLocation + "/" + dataName,"r")
        jsonFile = json.loads(f.read())
        return jsonify(status="success",response=jsonFile)
    except Exception as e:
        traceback.print_exc()
        return None


if __name__ == '__main__':
  app.run(port=8081)