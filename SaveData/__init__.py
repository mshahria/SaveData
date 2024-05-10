import azure.functions as func
import json

def main(req: func.HttpRequest, outputDocument: func.Out[func.Document]) -> func.HttpResponse:
    try:
        data = req.get_json()
        # Create a new document
        doc = func.Document.from_dict(data)
        outputDocument.set(doc)
        return func.HttpResponse("Document stored", status_code=200)
    except ValueError:
        return func.HttpResponse("Invalid JSON", status_code=400)



# import azure.functions as func
# import json

# def main(req: func.HttpRequest) -> func.HttpResponse:
#     try:
#         # Parse the JSON data from the request
#         data = req.get_json()
#         # Echo the received data back as a JSON response
#         return func.HttpResponse(json.dumps({
#             "status": "Received",
#             "data": data
#         }), mimetype="application/json", status_code=200)
#     except ValueError:
#         # If there is a JSON parsing error, return an error response
#         return func.HttpResponse("Invalid JSON", status_code=400)

# import azure.functions as func
# import os
# from azure.cosmos import CosmosClient, exceptions

# def main(req: func.HttpRequest) -> func.HttpResponse:
#     uri = os.environ['CosmosDB_URI']
#     key = os.environ['CosmosDB_KEY']
#     client = CosmosClient(uri, credential=key)
#     database = client.get_database_client('ChatData')
#     container = database.get_container_client('Sessions')

#     try:
#         # Read JSON payload from the request body and insert into Cosmos DB
#         data = req.get_json()
#         container.upsert_item(data)
#         return func.HttpResponse(status_code=204)  # No Content response
#     except ValueError:
#         # JSON is invalid
#         return func.HttpResponse(status_code=400)  # Bad Request response
#     except exceptions.CosmosHttpResponseError as e:
#         # Database operation failed
#         return func.HttpResponse(status_code=500)  # Internal Server Error response
