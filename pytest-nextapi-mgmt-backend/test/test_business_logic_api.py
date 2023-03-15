import requests
import json
from helper import get_base_url, get_token, get_tenant_id, get_api_id, get_unique_int_number, create_business_logic, get_business_logic, create_endpoint

BASE_URL = get_base_url()
tenant_id = get_tenant_id()
TOKEN = get_token()
api_id = get_api_id()
business_logic_id = "420"

def test_get_business_logic_list():
    payload = {
        "take":5,
        "skip":0,
        "page":1,
        "pageSize":5,
        "group":[]
    }
    response =  requests.post(BASE_URL + f"{tenant_id}/{api_id}/logic-grid", headers=TOKEN, json=payload)
    # data = response.json()
    # print(data)
    assert response.status_code == 200

    data = response.json()
    # print(data)
    assert data["total"] >= 0

def test_execute_business_logic():
    payload = {
        "logic":"context.outMessage.modified_by = \"Created and Edited by Pytest\";",
        "context":{
            "generic":{},
            "inMessage":{}
        }
    }
    response =  requests.post(BASE_URL + f"{tenant_id}/{api_id}/logic/exec", headers=TOKEN, json=payload)
    # data = response.json()
    # print(data)
    assert response.status_code == 200

    data = response.json()
    data_modified_by = data["outMessage"]["modified_by"]
    assert data_modified_by == "Created and Edited by Pytest"

def test_create_business_logic():
    random_number = get_unique_int_number()
    payload = {
        "Name": f"Business Logic Created by Pytest - {random_number}",
        "Description":"Created by Pytest",
        "Specification":{
            "script":"context.outMessage.modified_by = \"Created and Edited by Pytest\";",
            "fields":[
                {
                    "Name":"modified_by",
                    "Type":"string",
                    "FieldType":"output",
                    "ArrayMarker":"modified_by"
                }
            ]
        },
        "Shared":False
    }
    response = requests.post(BASE_URL + f"{tenant_id}/{api_id}/logic", headers=TOKEN, json=payload)
    # data = response.json()
    # print(data)
    # print(BASE_URL + f"{tenant_id}/{endpoint_id}/logic")
    assert response.status_code == 200

    data = response.json()
    data_name = data["Name"]
    assert data_name == f"Business Logic Created by Pytest - {random_number}"

def test_get_business_logic():
    response = requests.get(BASE_URL + f"{tenant_id}/{api_id}/logic/{business_logic_id}", headers=TOKEN)
    # data = response.json()
    # print(data)
    assert response.status_code == 200

    data = response.json()
    # print(data)
    assert data["Name"] == "Add Modified By"

def test_delete_business_logic():
    test_create_business_logic = create_business_logic()
    assert test_create_business_logic.status_code == 200
    test_create_business_logic_data = test_create_business_logic.json()
    test_create_business_logic_id = test_create_business_logic_data["ID"]

    response = requests.delete(BASE_URL + f"{tenant_id}/{api_id}/logic/{test_create_business_logic_id}", headers=TOKEN)
    assert response.status_code == 200

    test_get_business_logic = get_business_logic(test_create_business_logic_id)
    test_get_business_logic_data = test_get_business_logic.json()
    # print(test_get_business_logic_data)
    assert test_get_business_logic.status_code == 400
    assert test_get_business_logic_data["detail"] == "query Business Logic Definition failed: record not found"

def test_edit_business_logic():
    test_create_business_logic = create_business_logic()
    assert test_create_business_logic.status_code == 200
    test_create_business_logic_data = test_create_business_logic.json()
    test_create_business_logic_id = test_create_business_logic_data["ID"]
    test_create_business_logic_name = test_create_business_logic_data["Name"]

    payload = {
        "Name": test_create_business_logic_name,
        "Description":"Created and Edited by Pytest",
        "Specification":{
            "script":"context.outMessage.modified_by = \"Created and Edited by Pytest\";",
            "fields":[
                {
                    "Name":"modified_by",
                    "Type":"string",
                    "FieldType":"output",
                    "ArrayMarker":"modified_by"
                }
            ]
        },
        "Shared":False,
        "ID": test_create_business_logic_id
    }
    response = requests.put(BASE_URL + f"{tenant_id}/{api_id}/logic/{test_create_business_logic_id}", headers=TOKEN, json=payload)
    assert response.status_code == 200

    test_get_business_logic = get_business_logic(test_create_business_logic_id)
    test_get_business_logic_data = test_get_business_logic.json()
    # print(test_get_business_logic_data)
    assert test_get_business_logic.status_code == 200
    assert test_get_business_logic_data["Description"] == "Created and Edited by Pytest"

def test_get_endpoint_business_logic():
    endpoint_business_logic_id = "426"
    response = requests.get(BASE_URL + f"{tenant_id}/{api_id}/logic/endpoint/{endpoint_business_logic_id}", headers=TOKEN)
    # data = response.json()
    # print(data)
    assert response.status_code == 200

    data = response.json()
    # print(data)
    assert len(data) >= 0

def test_update_business_logic_endpoint():
    test_create_business_logic = create_business_logic()
    assert test_create_business_logic.status_code == 200
    test_create_business_logic_data = test_create_business_logic.json()
    test_create_business_logic_id = test_create_business_logic_data["ID"]
    test_create_business_logic_name = test_create_business_logic_data["Name"]
    test_create_business_logic_GlobalID = test_create_business_logic_data["GlobalID"]

    test_create_endpoint = create_endpoint()
    test_create_endpoint_data = test_create_endpoint.json()
    test_create_endpoint_name = test_create_endpoint_data["Name"]
    test_create_endpoint_id = test_create_endpoint_data["ID"]
    # print(test_create_endpoint_name)
    # print(test_create_endpoint_id)
    # print(test_create_business_logic_name)
    # print(test_create_business_logic_id)
    # print(test_create_business_logic_data)
    assert test_create_endpoint.status_code == 200

    update_pipeline_payload = {
        "Pipelines": [
            {
            "Tenant": "lab",
            "ID": 0,
            "No": 1,
            "IsStandalone": False,
            "Type": "rest_data_source",
            "Summary": "API Created By Pytest",
            "Specification": {
                "id": "ddbb23f0-b0f2-11ed-a717-12e419030aa5",
                "name": "API Created By Pytest",
                "method": "GET",
                "url": "https://reqres.in/api/users",
                "swagger": "2.0",
                "schemes": [
                "https"
                ],
                "produces": [
                "application/json"
                ],
                "consumes": [
                "raw"
                ],
                "host": "reqres.in",
                "basePath": "/api",
                "definitions": {},
                "paths": {
                "/users": {
                    "get": {
                    "shouldEscape": True,
                    "parameters": [
                        {
                        "name": "page",
                        "in": "query",
                        "type": "string"
                        }
                    ],
                    "responses": {
                        "200": {
                        "description": "successful operation",
                        "schema": {
                            "type": "object",
                            "properties": {
                            "page": {
                                "type": "number",
                                "format": "int32"
                            },
                            "per_page": {
                                "type": "number",
                                "format": "int32"
                            },
                            "total": {
                                "type": "number",
                                "format": "int32"
                            },
                            "total_pages": {
                                "type": "number",
                                "format": "int32"
                            },
                            "data": {
                                "type": "array",
                                "items": {
                                "type": "object",
                                "properties": {
                                    "id": {
                                    "type": "number",
                                    "format": "int32"
                                    },
                                    "email": {
                                    "type": "string"
                                    },
                                    "first_name": {
                                    "type": "string"
                                    },
                                    "last_name": {
                                    "type": "string"
                                    },
                                    "avatar": {
                                    "type": "string"
                                    }
                                }
                                }
                            },
                            "support": {
                                "type": "object",
                                "properties": {
                                "url": {
                                    "type": "string"
                                },
                                "text": {
                                    "type": "string"
                                }
                                }
                            }
                            }
                        }
                        }
                    },
                    "x-input-json": [],
                    "x-input-parameters": [
                        {
                        "from": {
                            "constant": 2
                        },
                        "to": {
                            "name": "page"
                        },
                        "type": "string",
                        "array_marker": [
                            "page"
                        ]
                        }
                    ],
                    "x-output-parameters": [
                        {
                        "from": {
                            "rest": [
                            "page"
                            ]
                        },
                        "to": {
                            "grpc_message": [
                            "page"
                            ]
                        },
                        "type": "int32",
                        "array_marker": [
                            "page"
                        ]
                        },
                        {
                        "from": {
                            "rest": [
                            "per_page"
                            ]
                        },
                        "to": {
                            "grpc_message": [
                            "per_page"
                            ]
                        },
                        "type": "int32",
                        "array_marker": [
                            "per_page"
                        ]
                        },
                        {
                        "from": {
                            "rest": [
                            "total"
                            ]
                        },
                        "to": {
                            "grpc_message": [
                            "total"
                            ]
                        },
                        "type": "int32",
                        "array_marker": [
                            "total"
                        ]
                        },
                        {
                        "from": {
                            "rest": [
                            "total_pages"
                            ]
                        },
                        "to": {
                            "grpc_message": [
                            "total_pages"
                            ]
                        },
                        "type": "int32",
                        "array_marker": [
                            "total_pages"
                        ]
                        },
                        {
                        "from": {
                            "rest": [
                            "data",
                            "id"
                            ]
                        },
                        "to": {
                            "grpc_message": [
                            "data",
                            "id"
                            ]
                        },
                        "type": "int32",
                        "array_marker": [
                            "*",
                            "id"
                        ]
                        },
                        {
                        "from": {
                            "rest": [
                            "data",
                            "email"
                            ]
                        },
                        "to": {
                            "grpc_message": [
                            "data",
                            "email"
                            ]
                        },
                        "type": "string",
                        "array_marker": [
                            "*",
                            "email"
                        ]
                        },
                        {
                        "from": {
                            "rest": [
                            "data",
                            "first_name"
                            ]
                        },
                        "to": {
                            "grpc_message": [
                            "data",
                            "first_name"
                            ]
                        },
                        "type": "string",
                        "array_marker": [
                            "*",
                            "first_name"
                        ]
                        },
                        {
                        "from": {
                            "rest": [
                            "data",
                            "last_name"
                            ]
                        },
                        "to": {
                            "grpc_message": [
                            "data",
                            "last_name"
                            ]
                        },
                        "type": "string",
                        "array_marker": [
                            "*",
                            "last_name"
                        ]
                        },
                        {
                        "from": {
                            "rest": [
                            "data",
                            "avatar"
                            ]
                        },
                        "to": {
                            "grpc_message": [
                            "data",
                            "avatar"
                            ]
                        },
                        "type": "string",
                        "array_marker": [
                            "*",
                            "avatar"
                        ]
                        },
                        {
                        "from": {
                            "rest": [
                            "support",
                            "url"
                            ]
                        },
                        "to": {
                            "grpc_message": [
                            "support",
                            "url"
                            ]
                        },
                        "type": "string",
                        "array_marker": [
                            "support",
                            "url"
                        ]
                        },
                        {
                        "from": {
                            "rest": [
                            "support",
                            "text"
                            ]
                        },
                        "to": {
                            "grpc_message": [
                            "support",
                            "text"
                            ]
                        },
                        "type": "string",
                        "array_marker": [
                            "support",
                            "text"
                        ]
                        }
                    ]
                    }
                }
                }
            },
            "EndpointID": test_create_endpoint_id
            },
            {
            "Tenant": "lab",
            "ID": 0,
            "No": 2,
            "IsStandalone": False,
            "Type": "business_logic",
            "Summary": "Add Modified By",
            "Specification": {
                "id": test_create_business_logic_GlobalID,
                "fields": [
                {
                    "Name": "modified_by",
                    "Type": "string",
                    "FieldType": "output",
                    "ArrayMarker": "modified_by"
                }
            ],
                "script": "context.outMessage.modified_by = \"Created and Edited by Pytest\";"
            },
            "EndpointID": test_create_endpoint_id
        }
        ]
    }
    update_pipeline = requests.put(BASE_URL + f"{tenant_id}/{test_create_endpoint_id}/pipelines/", headers=TOKEN, json=update_pipeline_payload)
    assert update_pipeline.status_code == 200

    edit_business_logic_payload = {
        "Name": test_create_business_logic_name,
        "Description":"Created and Edited by Pytest",
        "Specification":{
            "script":"context.outMessage.modified_by = \"Created and Edited by Pytest\";",
            "fields":[
                {
                    "Name":"modified_by",
                    "Type":"string",
                    "FieldType":"output",
                    "ArrayMarker":"modified_by"
                }
            ]
        },
        "Shared":False,
        "ID": test_create_business_logic_id
    }
    update_business_logic = requests.put(BASE_URL + f"{tenant_id}/{api_id}/logic/{test_create_business_logic_id}", headers=TOKEN, json=edit_business_logic_payload)
    assert update_business_logic.status_code == 200

    update_endpoint_business_logic_payload = {
        "Endp":[test_create_endpoint_id],
        "Spec":{
            "id":test_create_business_logic_GlobalID,
            "script":"context.outMessage.modified_by = \"Created and Edited by Pytest\";",
            "fields":[
                {
                    "Name":"modified_by",
                    "Type":"string",
                    "FieldType":"output",
                    "ArrayMarker":"modified_by"
                }
            ]
        }
    }
    update_business_logic = requests.post(BASE_URL + f"{tenant_id}/{api_id}/logic/updatebusinesslogic/{test_create_business_logic_id}", headers=TOKEN, json=update_endpoint_business_logic_payload)
    update_business_logic_data = update_business_logic.json()
    # print(update_business_logic_data)
    assert update_business_logic.status_code == 200
    assert update_business_logic_data["status"] == "succes"


    



