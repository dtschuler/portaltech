from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify
from funcmodule import run_detection

app = Flask(__name__)
api = Api(app)

class detection(Resource):
    def get(self):
        test_image_path = 'test-images/image1.jpg'
        fig_path = run_detection(test_image_path)
        print(fig_path)

api.add_resource(detection, '/detection') # Route_1

if __name__ == '__main__':
     app.run(port='5002')
     