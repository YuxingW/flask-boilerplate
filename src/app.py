from flask import Flask
from flask import render_template
from flask_pymongo import PyMongo
from flask_cors import cross_origin
from flask import jsonify
from flask import request
import json
from flask_sockets import Sockets


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://db:27017/automation_db"
mongo = PyMongo(app)

col = mongo.db["message_collection"]

@app.route('/hello')
@cross_origin(origin='*',headers=['access-control-allow-origin','Content-Type'])
def say_hello():
    """
    Say hello
    """
    response = {}
    response["status"] = str(200)
    response["data"] = "hello"
    return response

@app.route('/create_issue', methods = ['GET', 'POST'])
@cross_origin(origin='*',headers=['access-control-allow-origin','Content-Type'])
def create_issue():
    """
    Create a new issue, posted by Vew
    """
    issue = json.loads(request.get_data())
    print(issue)

    res = col.insert_one(issue)
    print(res)
    response = {}
    response["status"] = str(200)
    return response

@app.route('/query_issues')
@cross_origin(origin='*',headers=['access-control-allow-origin','Content-Type'])
def query_issues():
    """
    Query all the issues
    """
    data = []
    for doc in col.find():
      if '_id' in doc:
        del doc['_id']
      data.append(doc)
    response = {}
    response["status"] = str(200)
    response["data"] = data
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
