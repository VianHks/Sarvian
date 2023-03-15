import requests
import json
from helper import get_base_url, get_tenant_id, get_token, get_api_id, get_endpoint_id, get_unique_int_number, get_endpoint_by_id, create_endpoint, get_data_source, get_data_source_id, create_api_by_data_source, get_api_by_data_source_id

BASE_URL = get_base_url()
TOKEN = get_token()
tenant_id = get_tenant_id()
api_id = get_api_id()
data_source = get_data_source()

def test_get_api_by_data_source():
    payload = {
        "take":10,
        "skip":0,
        "page":1,
        "pageSize":10,
        "group":[]
    }
    response = requests.post(BASE_URL + f"{tenant_id}/{api_id}/filter-grid/{data_source}", headers=TOKEN, json=payload)
   # print(BASE_URL + f"{tenant_id}/api-grid")
    assert response.status_code == 200

    data = response.json()
    # print(data)
    assert len(data["data"]) >= 0

def test_get_api_by_data_source_id():
    data_source_id = get_data_source_id()
    response = requests.get(BASE_URL + f"{tenant_id}/{api_id}/filter/{data_source_id}", headers=TOKEN)
   # print(BASE_URL + f"{tenant_id}/api-grid")
    assert response.status_code == 200

    data = response.json()
    # print(data)
    assert data["Name"] == "Get Account"

def test_postman():
    payload = {
        "url":"https://accounting-api.cloud.nextplatform.ai/api/v1/accounting/accounts",
        "method":"GET",
        "qs":{},
        "headers":{},
        "form":{},
        "formData":{},
        "body":"{}",
        "no_redirect":True
    }
    response = requests.post(BASE_URL + f"{tenant_id}/postman", headers=TOKEN, json=payload)
    assert response.status_code == 200

    data = response.json()
    # print(data)
    test_currency_data = data["body"]["items"][0]["account_currency"]
    assert test_currency_data == "USD"

def test_create_api_by_data_source():
    number = get_unique_int_number()
    payload = {
        "Name": f"Pytest API - {number}",
        "Type": "rest_data_source",
        "Description": "API Created By Pytest",
        "Specification": {
            "method": "GET",
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
        }
    }
    response = requests.post(BASE_URL + f"{tenant_id}/{api_id}/filter/{data_source}", headers=TOKEN, json=payload)
    assert response.status_code == 200

    data = response.json()
    # print(data)
    API_ID_data = data["APIID"]
    assert API_ID_data == int(api_id)

def test_edit_api_by_data_source():
    create_api = create_api_by_data_source()
    assert create_api.status_code == 200
    
    create_api_data = create_api.json()
    create_api_name = create_api_data["Name"]
    create_api_id = create_api_data["ID"]

    payload = {
        "Name": f"{create_api_name}",
        "Type": "rest_data_source",
        "Description": "API Created and Edited By Pytest",
        "Specification": {
            "method": "GET",
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
                        "constant": 1
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
        }
    }
        
    response = requests.put(BASE_URL + f"{tenant_id}/{api_id}/filter/{data_source}/{create_api_id}", headers=TOKEN, json=payload)
    update_data = response.json()
    assert response.status_code == 200
    update_data_desc = update_data["Description"]

    test_get_api = get_api_by_data_source_id(create_api_id)
    assert test_get_api.status_code == 200
    test_get_api_data = test_get_api.json()
    test_get_api_desc = test_get_api_data["Description"]
    assert update_data_desc == test_get_api_desc

def test_delete_api_by_data_source_id():
    create_api = create_api_by_data_source()
    assert create_api.status_code == 200
    
    create_api_data = create_api.json()
    create_api_id = create_api_data["ID"]

    response = requests.delete(BASE_URL + f"{tenant_id}/{api_id}/filter/{create_api_id}", headers=TOKEN)
    assert response.status_code == 200

    test_get_api = get_api_by_data_source_id(create_api_id)
    test_get_api_data = test_get_api.json()
    assert test_get_api.status_code == 400
    assert test_get_api_data["detail"] == f"query Filter Definition ID {create_api_id} failed: record not found"

