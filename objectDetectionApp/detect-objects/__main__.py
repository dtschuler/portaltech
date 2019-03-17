from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify
from funcmodule import run_analysis

db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)

class detection(Resource):
    def get(self):
        fig_path = run_analysis()

api.add_resource(detection, '/detection') # Route_1