import azure.functions as func
from azure.cosmos import CosmosClient, exceptions
import os
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Get Cosmos DB client setup from environment variables
        endpoint = os.environ['COSMOS_ENDPOINT']
        key = os.environ['COSMOS_KEY']
        client = CosmosClient(endpoint, key)

        # Access the specific Cosmos DB database
        database_name = "SaveData"
        database = client.get_database_client(database=database_name)

        # Parse the JSON data from the request
        data = req.get_json()
        user_id = data['userId']  # Extract the userId from the received data

        # Prepare data to be stored
        store_data = {
            "sessionId": data["sessionId"],
            "chatHistory": data["chatHistory"]  # Assuming chatHistory is the key for questions and responses
        }

        # Access the container based on user_id and insert data
        container = database.get_container_client(user_id)
        # container.upsert_item(store_data)
        # container.upsert_item(
        #     dict(sessionId=data['sessionId'], chatHistory=data['chatHistory'])
        # )

        
        for container in database.list_containers():
            print("Container ID: {}".format(container['id']))

        return func.HttpResponse(
            json.dumps({"status": "Data stored successfully", "userId": data['userId'], "data": data['chatHistory']}),
            status_code=200,
            mimetype="application/json"
        )
    except ValueError:
        # If there is a JSON parsing error, return an error response
        return func.HttpResponse("Invalid JSON", status_code=400)
    except exceptions.CosmosHttpResponseError as e:
        # Handle Cosmos DB errors
        return func.HttpResponse(f"Error interacting with Cosmos DB: {str(e)}", status_code=500)
    except Exception as e:
        # Handle any other exceptions
        return func.HttpResponse(f"An error occurred: {str(e)}", status_code=500)






# import azure.functions as func
# import json

# def main(req: func.HttpRequest) -> func.HttpResponse:
#     try:
#         # Parse the JSON data from the request
#         data = req.get_json()
#         # Example processing: simply print or log the data
#         for qa_pair in data.get("chatHistory", []):
#             print(f"Question: {qa_pair['question']} Answer: {qa_pair['response']}")

#         # Echo the received data back as a JSON response
#         return func.HttpResponse(json.dumps({
#             "status": "Received",
#             "data": data
#         }), mimetype="application/json", status_code=200)
#     except ValueError:
#         # If there is a JSON parsing error, return an error response
#         return func.HttpResponse("Invalid JSON", status_code=400)




# import azure.functions as func
# import json

# def main(req: func.HttpRequest, outputDocument: func.Out[func.Document]) -> func.HttpResponse:
#     try:
#         data = req.get_json()
#         doc = func.Document.from_dict(data)
#         outputDocument.set(doc)
#         return func.HttpResponse("Document stored", status_code=200)
#     except ValueError as e:
#         return func.HttpResponse(f"Invalid JSON: {str(e)}", status_code=400)
#     except Exception as e:
#         return func.HttpResponse(f"Error: {str(e)}", status_code=500)


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
