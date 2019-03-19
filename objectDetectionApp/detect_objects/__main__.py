from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify
from funcmodule import run_detection

app = Flask(__name__)
api = Api(app)

@app.route('/detection/<path:s3_path>')
def detection(s3_path):
    tested_image_path = run_detection(s3_path)
    return(tested_image_path)

if __name__ == '__main__':
     app.run(debug = True, host = '0.0.0.0')
     