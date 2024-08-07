from flask import Flask
from flask_restful import Api, Resource
from ..resources.restrauntDetails import RestrauntDetails
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 
api = Api(app)

api.add_resource(RestrauntDetails, '/restraunts')