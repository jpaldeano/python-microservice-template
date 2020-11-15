''' Service start point '''
import os
from flask import Flask
from pymongo import MongoClient
from routes.health.health import HealthApi
from routes.v1.example.example import ExampleApi

def mustBuildMongoClient():
    mongoClient = MongoClient(os.environ.get("MONGO_CONNECTION_STRING"), \
    serverSelectionTimeoutMS=MONGO_TIMEOUT)

    return mongoClient

def mustBuildRoutes(flask_app, database):
    ''' mustBuildRoutes '''
    health_api = HealthApi(database)
    v1_example = ExampleApi(database)

    routes = [
        { 
            "path": "/health",
            "function": health_api.health,
            "method": "GET"
        },
        { 
            "path": "/v1/example",
            "function": v1_example.example,
            "method": "GET"
        },
    ]

    for route in routes:
        flask_app.add_url_rule(route["path"], view_func=route["function"], methods=[route["method"]])


if __name__ == "__main__":
    MONGO_TIMEOUT=10000
    app = Flask(__name__    )

    db = mustBuildMongoClient()
    mustBuildRoutes(app, db)

    app.run(host='0.0.0.0')
    