import azure.functions as func
import pymongo
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        # TODO: Update with appropriate MongoDB connection information
        url = "mongodb://cosmofunc277:t7DIYwejQRbOQRVd9Dg5VRLnpVHmJqkijlBFqjIZ0O6YeBqzvQQwO8DUFYCLoQyVaWKhuAQMB1BkACDbXns1kA==@cosmofunc277.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@cosmofunc277@"
        client = pymongo.MongoClient(url)
        database = client['azfunc2771']
        collection = database['advertisements']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)
