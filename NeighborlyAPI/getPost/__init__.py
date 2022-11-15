import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            # TODO: Update with appropriate MongoDB connection information
            url = "mongodb://cosmofunc277:t7DIYwejQRbOQRVd9Dg5VRLnpVHmJqkijlBFqjIZ0O6YeBqzvQQwO8DUFYCLoQyVaWKhuAQMB1BkACDbXns1kA==@cosmofunc277.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@cosmofunc277@"
            client = pymongo.MongoClient(url)
            database = client['azfunc2771']
            collection = database['posts']

            query = {'_id': ObjectId(id)}
            result = collection.find_one(query)
            result = dumps(result)

            return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
        except:
            return func.HttpResponse("Database connection error.", status_code=500)

    else:
        return func.HttpResponse("Please pass an id parameter in the query string.", status_code=400)
