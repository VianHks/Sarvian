import requests
import json
from helper import get_token, get_tenant_id, get_api_id, create_endpoint, get_base_url

BASE_URL = get_base_url()
endpoint_id = "3142"
tenant_id = get_tenant_id()
TOKEN = get_token()
api_id = get_api_id()

def test_get_pipelines_by_endpoint():
    response =  requests.get(BASE_URL + f"{tenant_id}/{endpoint_id}/pipelines", headers=TOKEN)
    assert response.status_code == 200

    data = response.json()
    # print(data)
    assert len(data) >= 0

def test_get_pipelines_auth_resource():
    response =  requests.get(BASE_URL + f"{tenant_id}/{endpoint_id}/pipelines/{api_id}/auth_resource", headers=TOKEN)
    assert response.status_code == 200

    data = response.json()
    # print(data)
    assert data == "Get_Account"

def test_edit_pipelines():
    test_create_endpoint = create_endpoint()
    assert test_create_endpoint.status_code == 200
    create_endpoint_data = test_create_endpoint.json()
    create_endpoint_id = create_endpoint_data["ID"]

    payload = {
        "Pipelines": [
            {
            "Tenant": "lab",
            "ID": 0,
            "No": 1,
            "IsStandalone": False,
            "Type": "rest_data_source",
            "Summary": "API Created By Pytest",
            "Specification": {
                "id": "73c8866b-b0f3-11ed-a717-12e419030aa5",
                "name": "Pytest API - 490",
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
                        },
                        {
                        "name": "body",
                        "in": "body",
                        "schema": {
                            "type": "object",
                            "properties": {}
                        }
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
                                "type": "undefined"
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
                            "constant": 3
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
                            "data"
                            ]
                        },
                        "to": {
                            "grpc_message": [
                            "data"
                            ]
                        },
                        "type": "",
                        "array_marker": [
                            "*"
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
            "EndpointID": create_endpoint_id
        }
        ]
    }
    response =  requests.put(BASE_URL + f"{tenant_id}/{create_endpoint_id}/pipelines/", headers=TOKEN, json=payload)
    assert response.status_code == 200

    data = response.json()
    # print(data)
    assert data['status'] == "succes"
