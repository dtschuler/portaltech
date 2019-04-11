from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify
from funcmodule import demo_portal_transaction

app = Flask(__name__)
api = Api(app)

@app.route('/detection/<path:s3_dir>')
def detection(s3_dir):
    transaction_demo_dict = demo_portal_transaction(s3_dir)
    return(jsonify(transaction_demo_dict))

if __name__ == '__main__':
     app.run(debug = True, host = '0.0.0.0')
     