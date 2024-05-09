import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse("Function is working properly", status_code=200)


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
