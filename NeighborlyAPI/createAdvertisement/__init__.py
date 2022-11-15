import azure.functions as func
import pymongo


def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()

    if request:
        try:
            # TODO: Update with appropriate MongoDB connection information
            url = "mongodb://cosmofunc277:t7DIYwejQRbOQRVd9Dg5VRLnpVHmJqkijlBFqjIZ0O6YeBqzvQQwO8DUFYCLoQyVaWKhuAQMB1BkACDbXns1kA==@cosmofunc277.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@cosmofunc277@"
            client = pymongo.MongoClient(url)
            database = client['azfunc2771']
            collection = database['advertisements']

            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )
