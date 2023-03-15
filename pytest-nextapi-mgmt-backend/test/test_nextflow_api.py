import requests
import json
from helper import create_endpoint, get_endpoint_by_id, get_token, get_tenant_id, get_api_id, get_base_url, get_data_source, get_unique_int_number, create_api_by_data_source, get_api_by_data_source_id

BASE_URL = get_base_url()
tenant_id = get_tenant_id()
TOKEN = get_token()
api_id = get_api_id()
data_source = get_data_source("nextflow")
data_source_template = get_data_source()

def test_get_nextflow_api_by_data_source():
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
    assert data["total"] >= 0

def test_get_nextflow_filter_template():
    payload = {
        "take":10,
        "skip":0,
        "page":1,
        "pageSize":10,
        "filter":{
            "logic":"and",
            "filters":[
                {
                    "field":"Name",
                    "operator":"eq",
                    "value":"NextFlow: Create Instance By ID V2"
                }
            ]
        },
        "sort":[
            {
                "field":"updated_at",
                "dir":"desc"
            }
        ],
        "group":[]
    }
    response = requests.post(BASE_URL + f"{tenant_id}/filtertpl/template-grid/{data_source_template}", headers=TOKEN, json=payload)
   # print(BASE_URL + f"{tenant_id}/api-grid")
    assert response.status_code == 200

    data = response.json()
    # print(data)
    assert data["total"] >= 0

def test_create_nextflow_api_by_data_source():
    number = get_unique_int_number()
    payload = {
        "Name": f"Pytest NextFlow - {number}",
        "Type": "nextflow",
        "Description": "Nextflow Created by Pytest",
        "Specification": {
            "method": "POST",
            "swagger": "2.0",
            "schemes": [
            "http"
            ],
            "produces": [
            "application/json"
            ],
            "consumes": [
            "application/json"
            ],
            "host": "taskmanager-api.cloud.nextplatform.ai",
            "basePath": "/demo/api",
            "definitions": {},
            "paths": {
            "/records": {
                "post": {
                "shouldEscape": True,
                "parameters": [
                    {
                    "name": "submit",
                    "in": "query",
                    "type": "string"
                    },
                    {
                    "name": "Authorization",
                    "in": "header",
                    "type": "string"
                    },
                    {
                    "name": "body",
                    "in": "body",
                    "schema": {
                        "type": "object",
                        "properties": {
                        "data": {
                            "type": "object",
                            "properties": {
                            "definition": {
                                "type": "object",
                                "properties": {
                                "id": {
                                    "type": "string"
                                }
                                }
                            },
                            "form_data": {
                                "type": "object",
                                "properties": {
                                "valid_registration": {
                                    "type": "boolean"
                                },
                                "confirmed": {
                                    "type": "boolean"
                                },
                                "tnkb_color": {
                                    "type": "string"
                                }
                                }
                            },
                            "comment": {
                                "type": "string"
                            }
                            }
                        }
                        }
                    }
                    }
                ],
                "responses": {
                    "200": {
                    "description": "successful operation",
                    "schema": {
                        "type": "object",
                        "properties": {
                        "data": {
                            "type": "object",
                            "properties": {
                            "id": {
                                "type": "string"
                            },
                            "entity": {
                                "type": "string"
                            },
                            "tenant_id": {
                                "type": "string"
                            },
                            "definition": {
                                "type": "object",
                                "properties": {
                                "id": {
                                    "type": "string"
                                },
                                "name": {
                                    "type": "string"
                                },
                                "category": {
                                    "type": "string"
                                },
                                "reference": {
                                    "type": "string"
                                },
                                "version": {
                                    "type": "string"
                                },
                                "type": {
                                    "type": "string"
                                },
                                "start_form_id": {
                                    "type": "string"
                                }
                                }
                            },
                            "instance_id": {
                                "type": "string"
                            },
                            "instance_ids": {
                                "type": "array",
                                "items": {
                                "type": "string"
                                }
                            },
                            "state": {
                                "type": "string"
                            },
                            "created_at": {
                                "type": "string"
                            },
                            "updated_at": {
                                "type": "string"
                            },
                            "created_by": {
                                "type": "object",
                                "properties": {
                                "id": {
                                    "type": "string"
                                },
                                "email": {
                                    "type": "string"
                                },
                                "name": {
                                    "type": "string"
                                }
                                }
                            },
                            "updated_by": {
                                "type": "object",
                                "properties": {
                                "id": {
                                    "type": "string"
                                },
                                "email": {
                                    "type": "string"
                                },
                                "name": {
                                    "type": "string"
                                }
                                }
                            },
                            "form_data": {
                                "type": "object",
                                "properties": {
                                "confirmed": {
                                    "type": "boolean"
                                },
                                "tnkb_color": {
                                    "type": "string"
                                },
                                "valid_registration": {
                                    "type": "boolean"
                                }
                                }
                            },
                            "variables": {
                                "type": "object",
                                "properties": {
                                "confirmed": {
                                    "type": "boolean"
                                },
                                "tnkb_color": {
                                    "type": "string"
                                },
                                "valid_registration": {
                                    "type": "boolean"
                                }
                                }
                            }
                            }
                        }
                        }
                    }
                    }
                },
                "x-input-json": [
                    {
                    "name": "inBody_data.definition.id",
                    "path": [
                        "data",
                        "definition",
                        "id"
                    ]
                    },
                    {
                    "name": "inBody_data.form_data",
                    "path": [
                        "data",
                        "form_data"
                    ]
                    },
                    {
                    "name": "inBody_data.comment",
                    "path": [
                        "data",
                        "comment"
                    ]
                    }
                ],
                "x-input-parameters": [
                    {
                    "from": {
                        "constant": "true"
                    },
                    "to": {
                        "name": "submit"
                    },
                    "type": "string",
                    "array_marker": [
                        "submit"
                    ],
                    "default": True
                    },
                    {
                    "from": {
                        "grpc_message": [
                        "authorization"
                        ]
                    },
                    "to": {
                        "name": "Authorization"
                    },
                    "type": "string",
                    "array_marker": [
                        "Authorization"
                    ],
                    "default": True
                    },
                    {
                    "from": {
                        "constant": "{{WORKFLOW_DEFINITION_ID}}"
                    },
                    "to": {
                        "name": "inBody_data.definition.id"
                    },
                    "type": "string",
                    "array_marker": [
                        "data",
                        "definition",
                        "id"
                    ],
                    "default": True
                    },
                    {
                    "from": {
                        "generic_context": "form_data_input"
                    },
                    "to": {
                        "name": "inBody_data.form_data"
                    },
                    "in": "body",
                    "path": [
                        "data",
                        "form_data"
                    ],
                    "default": True
                    },
                    {
                    "from": {
                        "grpc_message": [
                        "comment"
                        ]
                    },
                    "to": {
                        "name": "inBody_data.comment"
                    },
                    "type": "string",
                    "array_marker": [
                        "data",
                        "comment"
                    ],
                    "default": True
                    }
                ],
                "x-output-parameters": [
                    {
                    "default": True,
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
                    "type": "string",
                    "array_marker": [
                        "*",
                        "id"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "entity"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "entity"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "entity"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "tenant_id"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "tenant_id"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "tenant_id"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "definition",
                        "id"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "definition",
                        "id"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "definition",
                        "id"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "definition",
                        "name"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "definition",
                        "name"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "definition",
                        "name"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "definition",
                        "category"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "definition",
                        "category"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "definition",
                        "category"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "definition",
                        "reference"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "definition",
                        "reference"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "definition",
                        "reference"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "definition",
                        "version"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "definition",
                        "version"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "definition",
                        "version"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "definition",
                        "type"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "definition",
                        "type"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "definition",
                        "type"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "definition",
                        "start_form_id"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "definition",
                        "start_form_id"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "definition",
                        "start_form_id"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "instance_id"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "instance_id"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "instance_id"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "state"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "state"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "state"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "created_at"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "created_at"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "created_at"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "updated_at"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "updated_at"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "updated_at"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "completed_at"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "completed_at"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "completed_at"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "created_by",
                        "id"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "created_by",
                        "id"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "created_by",
                        "id"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "created_by",
                        "email"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "created_by",
                        "email"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "created_by",
                        "email"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "created_by",
                        "name"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "created_by",
                        "name"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "created_by",
                        "name"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "created_by",
                        "profile_picture"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "created_by",
                        "profile_picture"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "created_by",
                        "profile_picture"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "last_taskname"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "last_taskname"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "last_taskname"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "meta",
                        "response_count"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "meta",
                        "response_count"
                        ]
                    },
                    "type": "int32",
                    "array_marker": [
                        "meta",
                        "response_count"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "meta",
                        "total_count"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "meta",
                        "total_count"
                        ]
                    },
                    "type": "int32",
                    "array_marker": [
                        "meta",
                        "total_count"
                    ]
                    }
                ]
                }
            }
            },
            "x-nextflow-operation": "Create Instance By ID V2"
        }
    }
    response = requests.post(BASE_URL + f"{tenant_id}/{api_id}/filter/{data_source}", headers=TOKEN, json=payload)
    assert response.status_code == 200

    data = response.json()
    # print(data)
    # API_ID_data = data["APIID"]
    assert data["APIID"] == int(api_id)
    assert data["Name"] == f"Pytest NextFlow - {number}"

def test_edit_nextflow_api_by_data_source():
    create_api = create_api_by_data_source("nextflow")
    assert create_api.status_code == 200
    
    create_api_data = create_api.json()
    create_api_name = create_api_data["Name"]
    create_api_id = create_api_data["ID"]

    payload = {
        "Name": create_api_name,
        "Type": "nextflow",
        "Description": "Nextflow Created and Edited by Pytest",
        "Specification": {
            "method": "POST",
            "swagger": "2.0",
            "schemes": [
            "http"
            ],
            "produces": [
            "application/json"
            ],
            "consumes": [
            "application/json"
            ],
            "host": "taskmanager-api.cloud.nextplatform.ai",
            "basePath": "/demo/api",
            "definitions": {},
            "paths": {
            "/records": {
                "post": {
                "shouldEscape": True,
                "parameters": [
                    {
                    "name": "submit",
                    "in": "query",
                    "type": "string"
                    },
                    {
                    "name": "Authorization",
                    "in": "header",
                    "type": "string"
                    },
                    {
                    "name": "body",
                    "in": "body",
                    "schema": {
                        "type": "object",
                        "properties": {
                        "data": {
                            "type": "object",
                            "properties": {
                            "definition": {
                                "type": "object",
                                "properties": {
                                "id": {
                                    "type": "string"
                                }
                                }
                            },
                            "form_data": {
                                "type": "object",
                                "properties": {
                                "valid_registration": {
                                    "type": "boolean"
                                },
                                "confirmed": {
                                    "type": "boolean"
                                },
                                "tnkb_color": {
                                    "type": "string"
                                }
                                }
                            },
                            "comment": {
                                "type": "string"
                            }
                            }
                        }
                        }
                    }
                    }
                ],
                "responses": {
                    "200": {
                    "description": "successful operation",
                    "schema": {
                        "type": "object",
                        "properties": {
                        "data": {
                            "type": "object",
                            "properties": {
                            "id": {
                                "type": "string"
                            },
                            "entity": {
                                "type": "string"
                            },
                            "tenant_id": {
                                "type": "string"
                            },
                            "definition": {
                                "type": "object",
                                "properties": {
                                "id": {
                                    "type": "string"
                                },
                                "name": {
                                    "type": "string"
                                },
                                "category": {
                                    "type": "string"
                                },
                                "reference": {
                                    "type": "string"
                                },
                                "version": {
                                    "type": "string"
                                },
                                "type": {
                                    "type": "string"
                                },
                                "start_form_id": {
                                    "type": "string"
                                }
                                }
                            },
                            "instance_id": {
                                "type": "string"
                            },
                            "instance_ids": {
                                "type": "array",
                                "items": {
                                "type": "string"
                                }
                            },
                            "state": {
                                "type": "string"
                            },
                            "created_at": {
                                "type": "string"
                            },
                            "updated_at": {
                                "type": "string"
                            },
                            "created_by": {
                                "type": "object",
                                "properties": {
                                "id": {
                                    "type": "string"
                                },
                                "email": {
                                    "type": "string"
                                },
                                "name": {
                                    "type": "string"
                                }
                                }
                            },
                            "updated_by": {
                                "type": "object",
                                "properties": {
                                "id": {
                                    "type": "string"
                                },
                                "email": {
                                    "type": "string"
                                },
                                "name": {
                                    "type": "string"
                                }
                                }
                            },
                            "form_data": {
                                "type": "object",
                                "properties": {
                                "confirmed": {
                                    "type": "boolean"
                                },
                                "tnkb_color": {
                                    "type": "string"
                                },
                                "valid_registration": {
                                    "type": "boolean"
                                }
                                }
                            },
                            "variables": {
                                "type": "object",
                                "properties": {
                                "confirmed": {
                                    "type": "boolean"
                                },
                                "tnkb_color": {
                                    "type": "string"
                                },
                                "valid_registration": {
                                    "type": "boolean"
                                }
                                }
                            }
                            }
                        }
                        }
                    }
                    }
                },
                "x-input-json": [
                    {
                    "name": "inBody_data.definition.id",
                    "path": [
                        "data",
                        "definition",
                        "id"
                    ]
                    },
                    {
                    "name": "inBody_data.form_data",
                    "path": [
                        "data",
                        "form_data"
                    ]
                    },
                    {
                    "name": "inBody_data.comment",
                    "path": [
                        "data",
                        "comment"
                    ]
                    }
                ],
                "x-input-parameters": [
                    {
                    "from": {
                        "constant": "true"
                    },
                    "to": {
                        "name": "submit"
                    },
                    "type": "string",
                    "array_marker": [
                        "submit"
                    ],
                    "default": True
                    },
                    {
                    "from": {
                        "grpc_message": [
                        "authorization"
                        ]
                    },
                    "to": {
                        "name": "Authorization"
                    },
                    "type": "string",
                    "array_marker": [
                        "Authorization"
                    ],
                    "default": True
                    },
                    {
                    "from": {
                        "constant": "{{WORKFLOW_DEFINITION_ID}}"
                    },
                    "to": {
                        "name": "inBody_data.definition.id"
                    },
                    "type": "string",
                    "array_marker": [
                        "data",
                        "definition",
                        "id"
                    ],
                    "default": True
                    },
                    {
                    "from": {
                        "generic_context": "form_data_input"
                    },
                    "to": {
                        "name": "inBody_data.form_data"
                    },
                    "in": "body",
                    "path": [
                        "data",
                        "form_data"
                    ],
                    "default": True
                    },
                    {
                    "from": {
                        "grpc_message": [
                        "comment"
                        ]
                    },
                    "to": {
                        "name": "inBody_data.comment"
                    },
                    "type": "string",
                    "array_marker": [
                        "data",
                        "comment"
                    ],
                    "default": True
                    }
                ],
                "x-output-parameters": [
                    {
                    "default": True,
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
                    "type": "string",
                    "array_marker": [
                        "*",
                        "id"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "entity"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "entity"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "entity"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "tenant_id"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "tenant_id"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "tenant_id"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "definition",
                        "id"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "definition",
                        "id"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "definition",
                        "id"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "definition",
                        "name"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "definition",
                        "name"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "definition",
                        "name"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "definition",
                        "category"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "definition",
                        "category"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "definition",
                        "category"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "definition",
                        "reference"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "definition",
                        "reference"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "definition",
                        "reference"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "definition",
                        "version"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "definition",
                        "version"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "definition",
                        "version"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "definition",
                        "type"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "definition",
                        "type"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "definition",
                        "type"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "definition",
                        "start_form_id"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "definition",
                        "start_form_id"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "definition",
                        "start_form_id"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "instance_id"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "instance_id"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "instance_id"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "state"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "state"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "state"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "created_at"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "created_at"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "created_at"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "updated_at"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "updated_at"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "updated_at"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "completed_at"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "completed_at"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "completed_at"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "created_by",
                        "id"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "created_by",
                        "id"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "created_by",
                        "id"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "created_by",
                        "email"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "created_by",
                        "email"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "created_by",
                        "email"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "created_by",
                        "name"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "created_by",
                        "name"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "created_by",
                        "name"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "created_by",
                        "profile_picture"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "created_by",
                        "profile_picture"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "created_by",
                        "profile_picture"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "last_taskname"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "last_taskname"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "last_taskname"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "meta",
                        "response_count"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "meta",
                        "response_count"
                        ]
                    },
                    "type": "int32",
                    "array_marker": [
                        "meta",
                        "response_count"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "meta",
                        "total_count"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "meta",
                        "total_count"
                        ]
                    },
                    "type": "int32",
                    "array_marker": [
                        "meta",
                        "total_count"
                    ]
                    }
                ]
                }
            }
            },
            "x-nextflow-operation": "Create Instance By ID V2"
        }
    }
    response = requests.put(BASE_URL + f"{tenant_id}/{api_id}/filter/{data_source}/{create_api_id}", headers=TOKEN, json=payload)
    # update_data = response.json()
    # print(update_data)
    assert response.status_code == 200

    test_get_api = get_api_by_data_source_id(create_api_id)
    assert test_get_api.status_code == 200
    test_get_api_data = test_get_api.json()
    test_get_api_desc = test_get_api_data["Description"]
    assert test_get_api_desc == "Nextflow Created and Edited by Pytest"

def test_delete_nextflow_api_by_data_source_id():
    create_api = create_api_by_data_source("nextflow")
    assert create_api.status_code == 200
    
    create_api_data = create_api.json()
    create_api_id = create_api_data["ID"]

    response = requests.delete(BASE_URL + f"{tenant_id}/{api_id}/filter/{create_api_id}", headers=TOKEN)
    assert response.status_code == 200

    test_get_api = get_api_by_data_source_id(create_api_id)
    test_get_api_data = test_get_api.json()
    assert test_get_api.status_code == 400
    assert test_get_api_data["detail"] == f"query Filter Definition ID {create_api_id} failed: record not found"

def test_update_nextflow_endpoint():
    create_api = create_api_by_data_source("nextflow")
    assert create_api.status_code == 200
    
    create_api_data = create_api.json()
    create_api_name = create_api_data["Name"]
    create_api_id = create_api_data["ID"]
    create_api_global_id = create_api_data["GlobalID"]

    test_create_endpoint = create_endpoint("nextflow")
    test_create_endpoint_data = test_create_endpoint.json()
    # test_create_endpoint_name = test_create_endpoint_data["Name"]
    test_create_endpoint_id = test_create_endpoint_data["ID"]
    assert test_create_endpoint.status_code == 200

    update_pipeline_payload = {
        "Pipelines": [
            {
            "Tenant": "lab",
            "ID": 0,
            "No": 1,
            "IsStandalone": False,
            "Type": "nextflow",
            "Summary": "Nextflow Created by Pytest",
            "Specification": {
                "id": "5e98a8c4-bcc1-11ed-ad30-2ec8f1fe0b22",
                "name": "Pytest NextFlow - 217",
                "method": "POST",
                "swagger": "2.0",
                "schemes": [
                "http"
                ],
                "produces": [
                "application/json"
                ],
                "consumes": [
                "application/json"
                ],
                "host": "taskmanager-api.cloud.nextplatform.ai",
                "basePath": "/demo/api",
                "definitions": {},
                "paths": {
                "/records": {
                    "post": {
                    "shouldEscape": True,
                    "parameters": [
                        {
                        "name": "submit",
                        "in": "query",
                        "type": "string"
                        },
                        {
                        "name": "Authorization",
                        "in": "header",
                        "type": "string"
                        },
                        {
                        "name": "body",
                        "in": "body",
                        "schema": {
                            "type": "object",
                            "properties": {
                            "data": {
                                "type": "object",
                                "properties": {
                                "definition": {
                                    "type": "object",
                                    "properties": {
                                    "id": {
                                        "type": "string"
                                    }
                                    }
                                },
                                "form_data": {
                                    "type": "object",
                                    "properties": {
                                    "valid_registration": {
                                        "type": "boolean"
                                    },
                                    "confirmed": {
                                        "type": "boolean"
                                    },
                                    "tnkb_color": {
                                        "type": "string"
                                    }
                                    }
                                },
                                "comment": {
                                    "type": "string"
                                }
                                }
                            }
                            }
                        }
                        }
                    ],
                    "responses": {
                        "200": {
                        "description": "successful operation",
                        "schema": {
                            "type": "object",
                            "properties": {
                            "data": {
                                "type": "object",
                                "properties": {
                                "id": {
                                    "type": "string"
                                },
                                "entity": {
                                    "type": "string"
                                },
                                "tenant_id": {
                                    "type": "string"
                                },
                                "definition": {
                                    "type": "object",
                                    "properties": {
                                    "id": {
                                        "type": "string"
                                    },
                                    "name": {
                                        "type": "string"
                                    },
                                    "category": {
                                        "type": "string"
                                    },
                                    "reference": {
                                        "type": "string"
                                    },
                                    "version": {
                                        "type": "string"
                                    },
                                    "type": {
                                        "type": "string"
                                    },
                                    "start_form_id": {
                                        "type": "string"
                                    }
                                    }
                                },
                                "instance_id": {
                                    "type": "string"
                                },
                                "instance_ids": {
                                    "type": "array",
                                    "items": {
                                    "type": "string"
                                    }
                                },
                                "state": {
                                    "type": "string"
                                },
                                "created_at": {
                                    "type": "string"
                                },
                                "updated_at": {
                                    "type": "string"
                                },
                                "created_by": {
                                    "type": "object",
                                    "properties": {
                                    "id": {
                                        "type": "string"
                                    },
                                    "email": {
                                        "type": "string"
                                    },
                                    "name": {
                                        "type": "string"
                                    }
                                    }
                                },
                                "updated_by": {
                                    "type": "object",
                                    "properties": {
                                    "id": {
                                        "type": "string"
                                    },
                                    "email": {
                                        "type": "string"
                                    },
                                    "name": {
                                        "type": "string"
                                    }
                                    }
                                },
                                "form_data": {
                                    "type": "object",
                                    "properties": {
                                    "confirmed": {
                                        "type": "boolean"
                                    },
                                    "tnkb_color": {
                                        "type": "string"
                                    },
                                    "valid_registration": {
                                        "type": "boolean"
                                    }
                                    }
                                },
                                "variables": {
                                    "type": "object",
                                    "properties": {
                                    "confirmed": {
                                        "type": "boolean"
                                    },
                                    "tnkb_color": {
                                        "type": "string"
                                    },
                                    "valid_registration": {
                                        "type": "boolean"
                                    }
                                    }
                                }
                                }
                            }
                            }
                        }
                        }
                    },
                    "x-input-json": [
                        {
                        "name": "inBody_data.definition.id",
                        "path": [
                            "data",
                            "definition",
                            "id"
                        ]
                        },
                        {
                        "name": "inBody_data.form_data",
                        "path": [
                            "data",
                            "form_data"
                        ]
                        },
                        {
                        "name": "inBody_data.comment",
                        "path": [
                            "data",
                            "comment"
                        ]
                        }
                    ],
                    "x-input-parameters": [
                        {
                        "from": {
                            "constant": "true"
                        },
                        "to": {
                            "name": "submit"
                        },
                        "type": "string",
                        "array_marker": [
                            "submit"
                        ],
                        "default": True
                        },
                        {
                        "from": {
                            "grpc_message": [
                            "authorization"
                            ]
                        },
                        "to": {
                            "name": "Authorization"
                        },
                        "type": "string",
                        "array_marker": [
                            "Authorization"
                        ],
                        "default": True
                        },
                        {
                        "from": {
                            "constant": "{{WORKFLOW_DEFINITION_ID}}"
                        },
                        "to": {
                            "name": "inBody_data.definition.id"
                        },
                        "type": "string",
                        "array_marker": [
                            "data",
                            "definition",
                            "id"
                        ],
                        "default": True
                        },
                        {
                        "from": {
                            "generic_context": "form_data_input"
                        },
                        "to": {
                            "name": "inBody_data.form_data"
                        },
                        "in": "body",
                        "path": [
                            "data",
                            "form_data"
                        ],
                        "default": True
                        },
                        {
                        "from": {
                            "grpc_message": [
                            "comment"
                            ]
                        },
                        "to": {
                            "name": "inBody_data.comment"
                        },
                        "type": "string",
                        "array_marker": [
                            "data",
                            "comment"
                        ],
                        "default": True
                        }
                    ],
                    "x-output-parameters": [
                        {
                        "default": True,
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
                        "type": "string",
                        "array_marker": [
                            "*",
                            "id"
                        ]
                        },
                        {
                        "default": True,
                        "from": {
                            "rest": [
                            "data",
                            "entity"
                            ]
                        },
                        "to": {
                            "grpc_message": [
                            "data",
                            "entity"
                            ]
                        },
                        "type": "string",
                        "array_marker": [
                            "*",
                            "entity"
                        ]
                        },
                        {
                        "default": True,
                        "from": {
                            "rest": [
                            "data",
                            "tenant_id"
                            ]
                        },
                        "to": {
                            "grpc_message": [
                            "data",
                            "tenant_id"
                            ]
                        },
                        "type": "string",
                        "array_marker": [
                            "*",
                            "tenant_id"
                        ]
                        },
                        {
                        "default": True,
                        "from": {
                            "rest": [
                            "data",
                            "definition",
                            "id"
                            ]
                        },
                        "to": {
                            "grpc_message": [
                            "data",
                            "definition",
                            "id"
                            ]
                        },
                        "type": "string",
                        "array_marker": [
                            "*",
                            "definition",
                            "id"
                        ]
                        },
                        {
                        "default": True,
                        "from": {
                            "rest": [
                            "data",
                            "definition",
                            "name"
                            ]
                        },
                        "to": {
                            "grpc_message": [
                            "data",
                            "definition",
                            "name"
                            ]
                        },
                        "type": "string",
                        "array_marker": [
                            "*",
                            "definition",
                            "name"
                        ]
                        },
                        {
                        "default": True,
                        "from": {
                            "rest": [
                            "data",
                            "definition",
                            "category"
                            ]
                        },
                        "to": {
                            "grpc_message": [
                            "data",
                            "definition",
                            "category"
                            ]
                        },
                        "type": "string",
                        "array_marker": [
                            "*",
                            "definition",
                            "category"
                        ]
                        },
                        {
                        "default": True,
                        "from": {
                            "rest": [
                            "data",
                            "definition",
                            "reference"
                            ]
                        },
                        "to": {
                            "grpc_message": [
                            "data",
                            "definition",
                            "reference"
                            ]
                        },
                        "type": "string",
                        "array_marker": [
                            "*",
                            "definition",
                            "reference"
                        ]
                        },
                        {
                        "default": True,
                        "from": {
                            "rest": [
                            "data",
                            "definition",
                            "version"
                            ]
                        },
                        "to": {
                            "grpc_message": [
                            "data",
                            "definition",
                            "version"
                            ]
                        },
                        "type": "string",
                        "array_marker": [
                            "*",
                            "definition",
                            "version"
                        ]
                        },
                        {
                        "default": True,
                        "from": {
                            "rest": [
                            "data",
                            "definition",
                            "type"
                            ]
                        },
                        "to": {
                            "grpc_message": [
                            "data",
                            "definition",
                            "type"
                            ]
                        },
                        "type": "string",
                        "array_marker": [
                            "*",
                            "definition",
                            "type"
                        ]
                        },
                        {
                        "default": True,
                        "from": {
                            "rest": [
                            "data",
                            "definition",
                            "start_form_id"
                            ]
                        },
                        "to": {
                            "grpc_message": [
                            "data",
                            "definition",
                            "start_form_id"
                            ]
                        },
                        "type": "string",
                        "array_marker": [
                            "*",
                            "definition",
                            "start_form_id"
                        ]
                        },
                        {
                        "default": True,
                        "from": {
                            "rest": [
                            "data",
                            "instance_id"
                            ]
                        },
                        "to": {
                            "grpc_message": [
                            "data",
                            "instance_id"
                            ]
                        },
                        "type": "string",
                        "array_marker": [
                            "*",
                            "instance_id"
                        ]
                        },
                        {
                        "default": True,
                        "from": {
                            "rest": [
                            "data",
                            "state"
                            ]
                        },
                        "to": {
                            "grpc_message": [
                            "data",
                            "state"
                            ]
                        },
                        "type": "string",
                        "array_marker": [
                            "*",
                            "state"
                        ]
                        },
                        {
                        "default": True,
                        "from": {
                            "rest": [
                            "data",
                            "created_at"
                            ]
                        },
                        "to": {
                            "grpc_message": [
                            "data",
                            "created_at"
                            ]
                        },
                        "type": "string",
                        "array_marker": [
                            "*",
                            "created_at"
                        ]
                        },
                        {
                        "default": True,
                        "from": {
                            "rest": [
                            "data",
                            "updated_at"
                            ]
                        },
                        "to": {
                            "grpc_message": [
                            "data",
                            "updated_at"
                            ]
                        },
                        "type": "string",
                        "array_marker": [
                            "*",
                            "updated_at"
                        ]
                        },
                        {
                        "default": True,
                        "from": {
                            "rest": [
                            "data",
                            "completed_at"
                            ]
                        },
                        "to": {
                            "grpc_message": [
                            "data",
                            "completed_at"
                            ]
                        },
                        "type": "string",
                        "array_marker": [
                            "*",
                            "completed_at"
                        ]
                        },
                        {
                        "default": True,
                        "from": {
                            "rest": [
                            "data",
                            "created_by",
                            "id"
                            ]
                        },
                        "to": {
                            "grpc_message": [
                            "data",
                            "created_by",
                            "id"
                            ]
                        },
                        "type": "string",
                        "array_marker": [
                            "*",
                            "created_by",
                            "id"
                        ]
                        },
                        {
                        "default": True,
                        "from": {
                            "rest": [
                            "data",
                            "created_by",
                            "email"
                            ]
                        },
                        "to": {
                            "grpc_message": [
                            "data",
                            "created_by",
                            "email"
                            ]
                        },
                        "type": "string",
                        "array_marker": [
                            "*",
                            "created_by",
                            "email"
                        ]
                        },
                        {
                        "default": True,
                        "from": {
                            "rest": [
                            "data",
                            "created_by",
                            "name"
                            ]
                        },
                        "to": {
                            "grpc_message": [
                            "data",
                            "created_by",
                            "name"
                            ]
                        },
                        "type": "string",
                        "array_marker": [
                            "*",
                            "created_by",
                            "name"
                        ]
                        },
                        {
                        "default": True,
                        "from": {
                            "rest": [
                            "data",
                            "created_by",
                            "profile_picture"
                            ]
                        },
                        "to": {
                            "grpc_message": [
                            "data",
                            "created_by",
                            "profile_picture"
                            ]
                        },
                        "type": "string",
                        "array_marker": [
                            "*",
                            "created_by",
                            "profile_picture"
                        ]
                        },
                        {
                        "default": True,
                        "from": {
                            "rest": [
                            "data",
                            "last_taskname"
                            ]
                        },
                        "to": {
                            "grpc_message": [
                            "data",
                            "last_taskname"
                            ]
                        },
                        "type": "string",
                        "array_marker": [
                            "*",
                            "last_taskname"
                        ]
                        },
                        {
                        "default": True,
                        "from": {
                            "rest": [
                            "meta",
                            "response_count"
                            ]
                        },
                        "to": {
                            "grpc_message": [
                            "meta",
                            "response_count"
                            ]
                        },
                        "type": "int32",
                        "array_marker": [
                            "meta",
                            "response_count"
                        ]
                        },
                        {
                        "default": True,
                        "from": {
                            "rest": [
                            "meta",
                            "total_count"
                            ]
                        },
                        "to": {
                            "grpc_message": [
                            "meta",
                            "total_count"
                            ]
                        },
                        "type": "int32",
                        "array_marker": [
                            "meta",
                            "total_count"
                        ]
                        }
                    ]
                    }
                }
                },
                "x-nextflow-operation": "Create Instance By ID V2"
            },
            "EndpointID": int(test_create_endpoint_id)
            }
        ]
    }
    update_pipeline = requests.put(BASE_URL + f"{tenant_id}/{test_create_endpoint_id}/pipelines/", headers=TOKEN, json=update_pipeline_payload)
    assert update_pipeline.status_code == 200

    edit_nextflow_payload = {
        "Name": create_api_name,
        "Type": "nextflow",
        "Description": "Nextflow Created and Edited by Pytest",
        "Specification": {
            "method": "POST",
            "swagger": "2.0",
            "schemes": [
            "http"
            ],
            "produces": [
            "application/json"
            ],
            "consumes": [
            "application/json"
            ],
            "host": "taskmanager-api.cloud.nextplatform.ai",
            "basePath": "/demo/api",
            "definitions": {},
            "paths": {
            "/records": {
                "post": {
                "shouldEscape": True,
                "parameters": [
                    {
                    "name": "submit",
                    "in": "query",
                    "type": "string"
                    },
                    {
                    "name": "Authorization",
                    "in": "header",
                    "type": "string"
                    },
                    {
                    "name": "body",
                    "in": "body",
                    "schema": {
                        "type": "object",
                        "properties": {
                        "data": {
                            "type": "object",
                            "properties": {
                            "definition": {
                                "type": "object",
                                "properties": {
                                "id": {
                                    "type": "string"
                                }
                                }
                            },
                            "form_data": {
                                "type": "object",
                                "properties": {
                                "valid_registration": {
                                    "type": "boolean"
                                },
                                "confirmed": {
                                    "type": "boolean"
                                },
                                "tnkb_color": {
                                    "type": "string"
                                }
                                }
                            },
                            "comment": {
                                "type": "string"
                            }
                            }
                        }
                        }
                    }
                    }
                ],
                "responses": {
                    "200": {
                    "description": "successful operation",
                    "schema": {
                        "type": "object",
                        "properties": {
                        "data": {
                            "type": "object",
                            "properties": {
                            "id": {
                                "type": "string"
                            },
                            "entity": {
                                "type": "string"
                            },
                            "tenant_id": {
                                "type": "string"
                            },
                            "definition": {
                                "type": "object",
                                "properties": {
                                "id": {
                                    "type": "string"
                                },
                                "name": {
                                    "type": "string"
                                },
                                "category": {
                                    "type": "string"
                                },
                                "reference": {
                                    "type": "string"
                                },
                                "version": {
                                    "type": "string"
                                },
                                "type": {
                                    "type": "string"
                                },
                                "start_form_id": {
                                    "type": "string"
                                }
                                }
                            },
                            "instance_id": {
                                "type": "string"
                            },
                            "instance_ids": {
                                "type": "array",
                                "items": {
                                "type": "string"
                                }
                            },
                            "state": {
                                "type": "string"
                            },
                            "created_at": {
                                "type": "string"
                            },
                            "updated_at": {
                                "type": "string"
                            },
                            "created_by": {
                                "type": "object",
                                "properties": {
                                "id": {
                                    "type": "string"
                                },
                                "email": {
                                    "type": "string"
                                },
                                "name": {
                                    "type": "string"
                                }
                                }
                            },
                            "updated_by": {
                                "type": "object",
                                "properties": {
                                "id": {
                                    "type": "string"
                                },
                                "email": {
                                    "type": "string"
                                },
                                "name": {
                                    "type": "string"
                                }
                                }
                            },
                            "form_data": {
                                "type": "object",
                                "properties": {
                                "confirmed": {
                                    "type": "boolean"
                                },
                                "tnkb_color": {
                                    "type": "string"
                                },
                                "valid_registration": {
                                    "type": "boolean"
                                }
                                }
                            },
                            "variables": {
                                "type": "object",
                                "properties": {
                                "confirmed": {
                                    "type": "boolean"
                                },
                                "tnkb_color": {
                                    "type": "string"
                                },
                                "valid_registration": {
                                    "type": "boolean"
                                }
                                }
                            }
                            }
                        }
                        }
                    }
                    }
                },
                "x-input-json": [
                    {
                    "name": "inBody_data.definition.id",
                    "path": [
                        "data",
                        "definition",
                        "id"
                    ]
                    },
                    {
                    "name": "inBody_data.form_data",
                    "path": [
                        "data",
                        "form_data"
                    ]
                    },
                    {
                    "name": "inBody_data.comment",
                    "path": [
                        "data",
                        "comment"
                    ]
                    }
                ],
                "x-input-parameters": [
                    {
                    "from": {
                        "constant": "true"
                    },
                    "to": {
                        "name": "submit"
                    },
                    "type": "string",
                    "array_marker": [
                        "submit"
                    ],
                    "default": True
                    },
                    {
                    "from": {
                        "grpc_message": [
                        "authorization"
                        ]
                    },
                    "to": {
                        "name": "Authorization"
                    },
                    "type": "string",
                    "array_marker": [
                        "Authorization"
                    ],
                    "default": True
                    },
                    {
                    "from": {
                        "constant": "{{WORKFLOW_DEFINITION_ID}}"
                    },
                    "to": {
                        "name": "inBody_data.definition.id"
                    },
                    "type": "string",
                    "array_marker": [
                        "data",
                        "definition",
                        "id"
                    ],
                    "default": True
                    },
                    {
                    "from": {
                        "generic_context": "form_data_input"
                    },
                    "to": {
                        "name": "inBody_data.form_data"
                    },
                    "in": "body",
                    "path": [
                        "data",
                        "form_data"
                    ],
                    "default": True
                    },
                    {
                    "from": {
                        "grpc_message": [
                        "comment"
                        ]
                    },
                    "to": {
                        "name": "inBody_data.comment"
                    },
                    "type": "string",
                    "array_marker": [
                        "data",
                        "comment"
                    ],
                    "default": True
                    }
                ],
                "x-output-parameters": [
                    {
                    "default": True,
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
                    "type": "string",
                    "array_marker": [
                        "*",
                        "id"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "entity"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "entity"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "entity"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "tenant_id"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "tenant_id"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "tenant_id"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "definition",
                        "id"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "definition",
                        "id"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "definition",
                        "id"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "definition",
                        "name"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "definition",
                        "name"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "definition",
                        "name"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "definition",
                        "category"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "definition",
                        "category"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "definition",
                        "category"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "definition",
                        "reference"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "definition",
                        "reference"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "definition",
                        "reference"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "definition",
                        "version"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "definition",
                        "version"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "definition",
                        "version"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "definition",
                        "type"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "definition",
                        "type"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "definition",
                        "type"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "definition",
                        "start_form_id"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "definition",
                        "start_form_id"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "definition",
                        "start_form_id"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "instance_id"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "instance_id"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "instance_id"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "state"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "state"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "state"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "created_at"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "created_at"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "created_at"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "updated_at"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "updated_at"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "updated_at"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "completed_at"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "completed_at"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "completed_at"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "created_by",
                        "id"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "created_by",
                        "id"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "created_by",
                        "id"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "created_by",
                        "email"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "created_by",
                        "email"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "created_by",
                        "email"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "created_by",
                        "name"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "created_by",
                        "name"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "created_by",
                        "name"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "created_by",
                        "profile_picture"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "created_by",
                        "profile_picture"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "created_by",
                        "profile_picture"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "last_taskname"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "last_taskname"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "last_taskname"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "meta",
                        "response_count"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "meta",
                        "response_count"
                        ]
                    },
                    "type": "int32",
                    "array_marker": [
                        "meta",
                        "response_count"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "meta",
                        "total_count"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "meta",
                        "total_count"
                        ]
                    },
                    "type": "int32",
                    "array_marker": [
                        "meta",
                        "total_count"
                    ]
                    }
                ]
                }
            }
            },
            "x-nextflow-operation": "Create Instance By ID V2"
        }
    }
    update_nextflow = requests.put(BASE_URL + f"{tenant_id}/{api_id}/filter/{data_source}/{create_api_id}", headers=TOKEN, json=edit_nextflow_payload)
    assert update_nextflow.status_code == 200

    update_endpoint_nextflow_payload = {
        "Endp": [
            int(test_create_endpoint_id)
        ],
        "Spec": {
            "method": "POST",
            "swagger": "2.0",
            "schemes": [
            "http"
            ],
            "produces": [
            "application/json"
            ],
            "consumes": [
            "application/json"
            ],
            "host": "taskmanager-api.cloud.nextplatform.ai",
            "basePath": "/demo/api",
            "definitions": {},
            "paths": {
            "/records": {
                "post": {
                "shouldEscape": True,
                "parameters": [
                    {
                    "name": "submit",
                    "in": "query",
                    "type": "string"
                    },
                    {
                    "name": "Authorization",
                    "in": "header",
                    "type": "string"
                    },
                    {
                    "name": "body",
                    "in": "body",
                    "schema": {
                        "type": "object",
                        "properties": {
                        "data": {
                            "type": "object",
                            "properties": {
                            "definition": {
                                "type": "object",
                                "properties": {
                                "id": {
                                    "type": "string"
                                }
                                }
                            },
                            "form_data": {
                                "type": "object",
                                "properties": {
                                "valid_registration": {
                                    "type": "boolean"
                                },
                                "confirmed": {
                                    "type": "boolean"
                                },
                                "tnkb_color": {
                                    "type": "string"
                                }
                                }
                            },
                            "comment": {
                                "type": "string"
                            }
                            }
                        }
                        }
                    }
                    }
                ],
                "responses": {
                    "200": {
                    "description": "successful operation",
                    "schema": {
                        "type": "object",
                        "properties": {
                        "data": {
                            "type": "object",
                            "properties": {
                            "id": {
                                "type": "string"
                            },
                            "entity": {
                                "type": "string"
                            },
                            "tenant_id": {
                                "type": "string"
                            },
                            "definition": {
                                "type": "object",
                                "properties": {
                                "id": {
                                    "type": "string"
                                },
                                "name": {
                                    "type": "string"
                                },
                                "category": {
                                    "type": "string"
                                },
                                "reference": {
                                    "type": "string"
                                },
                                "version": {
                                    "type": "string"
                                },
                                "type": {
                                    "type": "string"
                                },
                                "start_form_id": {
                                    "type": "string"
                                }
                                }
                            },
                            "instance_id": {
                                "type": "string"
                            },
                            "instance_ids": {
                                "type": "array",
                                "items": {
                                "type": "string"
                                }
                            },
                            "state": {
                                "type": "string"
                            },
                            "created_at": {
                                "type": "string"
                            },
                            "updated_at": {
                                "type": "string"
                            },
                            "created_by": {
                                "type": "object",
                                "properties": {
                                "id": {
                                    "type": "string"
                                },
                                "email": {
                                    "type": "string"
                                },
                                "name": {
                                    "type": "string"
                                }
                                }
                            },
                            "updated_by": {
                                "type": "object",
                                "properties": {
                                "id": {
                                    "type": "string"
                                },
                                "email": {
                                    "type": "string"
                                },
                                "name": {
                                    "type": "string"
                                }
                                }
                            },
                            "form_data": {
                                "type": "object",
                                "properties": {
                                "confirmed": {
                                    "type": "boolean"
                                },
                                "tnkb_color": {
                                    "type": "string"
                                },
                                "valid_registration": {
                                    "type": "boolean"
                                }
                                }
                            },
                            "variables": {
                                "type": "object",
                                "properties": {
                                "confirmed": {
                                    "type": "boolean"
                                },
                                "tnkb_color": {
                                    "type": "string"
                                },
                                "valid_registration": {
                                    "type": "boolean"
                                }
                                }
                            }
                            }
                        }
                        }
                    }
                    }
                },
                "x-input-json": [
                    {
                    "name": "inBody_data.definition.id",
                    "path": [
                        "data",
                        "definition",
                        "id"
                    ]
                    },
                    {
                    "name": "inBody_data.form_data",
                    "path": [
                        "data",
                        "form_data"
                    ]
                    },
                    {
                    "name": "inBody_data.comment",
                    "path": [
                        "data",
                        "comment"
                    ]
                    }
                ],
                "x-input-parameters": [
                    {
                    "from": {
                        "constant": "true"
                    },
                    "to": {
                        "name": "submit"
                    },
                    "type": "string",
                    "array_marker": [
                        "submit"
                    ],
                    "default": True
                    },
                    {
                    "from": {
                        "grpc_message": [
                        "authorization"
                        ]
                    },
                    "to": {
                        "name": "Authorization"
                    },
                    "type": "string",
                    "array_marker": [
                        "Authorization"
                    ],
                    "default": True
                    },
                    {
                    "from": {
                        "constant": "{{WORKFLOW_DEFINITION_ID}}"
                    },
                    "to": {
                        "name": "inBody_data.definition.id"
                    },
                    "type": "string",
                    "array_marker": [
                        "data",
                        "definition",
                        "id"
                    ],
                    "default": True
                    },
                    {
                    "from": {
                        "generic_context": "form_data_input"
                    },
                    "to": {
                        "name": "inBody_data.form_data"
                    },
                    "in": "body",
                    "path": [
                        "data",
                        "form_data"
                    ],
                    "default": True
                    },
                    {
                    "from": {
                        "grpc_message": [
                        "comment"
                        ]
                    },
                    "to": {
                        "name": "inBody_data.comment"
                    },
                    "type": "string",
                    "array_marker": [
                        "data",
                        "comment"
                    ],
                    "default": True
                    }
                ],
                "x-output-parameters": [
                    {
                    "default": True,
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
                    "type": "string",
                    "array_marker": [
                        "*",
                        "id"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "entity"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "entity"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "entity"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "tenant_id"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "tenant_id"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "tenant_id"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "definition",
                        "id"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "definition",
                        "id"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "definition",
                        "id"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "definition",
                        "name"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "definition",
                        "name"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "definition",
                        "name"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "definition",
                        "category"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "definition",
                        "category"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "definition",
                        "category"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "definition",
                        "reference"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "definition",
                        "reference"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "definition",
                        "reference"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "definition",
                        "version"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "definition",
                        "version"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "definition",
                        "version"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "definition",
                        "type"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "definition",
                        "type"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "definition",
                        "type"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "definition",
                        "start_form_id"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "definition",
                        "start_form_id"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "definition",
                        "start_form_id"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "instance_id"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "instance_id"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "instance_id"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "state"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "state"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "state"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "created_at"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "created_at"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "created_at"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "updated_at"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "updated_at"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "updated_at"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "completed_at"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "completed_at"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "completed_at"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "created_by",
                        "id"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "created_by",
                        "id"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "created_by",
                        "id"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "created_by",
                        "email"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "created_by",
                        "email"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "created_by",
                        "email"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "created_by",
                        "name"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "created_by",
                        "name"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "created_by",
                        "name"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "created_by",
                        "profile_picture"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "created_by",
                        "profile_picture"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "created_by",
                        "profile_picture"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "data",
                        "last_taskname"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "data",
                        "last_taskname"
                        ]
                    },
                    "type": "string",
                    "array_marker": [
                        "*",
                        "last_taskname"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "meta",
                        "response_count"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "meta",
                        "response_count"
                        ]
                    },
                    "type": "int32",
                    "array_marker": [
                        "meta",
                        "response_count"
                    ]
                    },
                    {
                    "default": True,
                    "from": {
                        "rest": [
                        "meta",
                        "total_count"
                        ]
                    },
                    "to": {
                        "grpc_message": [
                        "meta",
                        "total_count"
                        ]
                    },
                    "type": "int32",
                    "array_marker": [
                        "meta",
                        "total_count"
                    ]
                    }
                ]
                }
            }
            },
            "x-nextflow-operation": "Create Instance By ID V2",
            "id": create_api_global_id
        }
    }
    update_nextflow = requests.post(BASE_URL + f"{tenant_id}/{api_id}/filter/updatefilter/{data_source}/{create_api_id}", headers=TOKEN, json=update_endpoint_nextflow_payload)
    update_nextflow_data = update_nextflow.json()
    # print(update_nextflow_data)
    assert update_nextflow.status_code == 200
    assert update_nextflow_data["status"] == "succes"


