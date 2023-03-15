import requests
import json
import random

BASE_URL = "https://nextapi-mgmt-api.lab.nextplatform.ai/v1/"
CUSTOM_FUNCTION_URL = "https://faas-mgmt-api.lab.nextplatform.ai/v1/api/"
BUSINESS_RULE_URL = "https://repository.lab.nextplatform.ai/"
TOKEN = {"Authorization": "Bearer ory_at_JrXCCOP4shWzE3a1UVzJiNMc-kW6YBPnJREJiKV3dXM._fNFi8L__VSbyjaf5f8YhfFcrHVmSoHVxrkjyieddNQ"}
tenant_id = "lab"
api_id = "385"
api_redis_id="398"
data_source = "rest_data_source"
faas_data_source = "faas"
soap_data_source = "soap_data_source"
nextbytes_data_source = "next_bytes"
nextbytes_doc_generator_data_source = "next_bytes,document_generator"
document_generator_data_source = "document_generator"
arangodb_data_source = "arangodb_data_source"
nextflow_data_source = "nextflow"
connection_id = "67"
dmn_id = "files:dmn:84a1132e-8634-4dcf-9bfe-ba20ff1d3492"

def get_base_url(url_type=None):
    if url_type is None:
        url = BASE_URL
    elif url_type == "business_rule":
        url = BUSINESS_RULE_URL
    elif url_type == "custom_function":
        url = CUSTOM_FUNCTION_URL
    return url

def get_dmn_id():
    return dmn_id

def get_connection_id():
    return connection_id

def get_data_source(input_data_source=None):
    if input_data_source is None:
        return_data_source = data_source
    elif input_data_source == "faas":
        return_data_source = faas_data_source
    elif input_data_source == "soap":
        return_data_source = soap_data_source
    elif input_data_source == "arangodb":
        return_data_source = arangodb_data_source
    elif input_data_source == "nextbytes_send_email":
        return_data_source = nextbytes_data_source
    elif input_data_source == "nextbytes_doc_generator":
        return_data_source = document_generator_data_source
    elif input_data_source == "nextbytes,doc":
        return_data_source = nextbytes_doc_generator_data_source
    elif input_data_source == "nextflow":
        return_data_source = "nextflow"
    elif input_data_source == "redis":
        return_data_source = "redis"
    return return_data_source

def get_token():
    return TOKEN

def get_tenant_id():
    return tenant_id

def get_api_id():
    return api_id

def get_endpoint_id():
    response = requests.get(BASE_URL + f"{tenant_id}/{api_id}/endpoint/", headers=TOKEN)
    assert response.status_code == 200

    get_endpoint_data = response.json()
    return get_endpoint_data[0]["ID"]

def get_unique_int_number():
    return random.randint(0, 999)

def get_api_by_id(test_api_id):
    return requests.get(BASE_URL + f"{tenant_id}/api/{test_api_id}", headers=TOKEN)

def get_endpoint_by_id(test_endpoint_id):
    return requests.get(BASE_URL + f"{tenant_id}/{api_id}/endpoint/{test_endpoint_id}", headers=TOKEN)

def create_endpoint(input_data_source=None):
    random_number = get_unique_int_number()
    if input_data_source is not None:
        if input_data_source == "arangodb":
            endpoint_name = f"Pytest ArangoDB Endpoint - {random_number}"
        elif input_data_source == "nextbytes_send_email":
            endpoint_name = f"Pytest Nextbytes Send Email Endpoint - {random_number}"
        elif input_data_source == "nextbytes_doc_generator":
            endpoint_name = f"Pytest Nextbytes Doc Generator Endpoint - {random_number}"
        elif input_data_source == "nextflow":
            endpoint_name = f"Pytest Nextflow Endpoint - {random_number}"
    else:
        endpoint_name = f"Pytest Create Endpoint - {random_number}"
    
    payload = {
        "Type":"custom",
        "Name": endpoint_name,
        "Summary":"Endpoint created by pytest",
        "ResourceName":"",
        "RESTMethod":"",
        "LogLevel":""
    }

    return requests.post(BASE_URL + f"{tenant_id}/{api_id}/endpoint", headers=TOKEN, json=payload)

def get_data_source_id():
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
    data_source_id = data["data"][0]["id"]
    return data_source_id

def get_api_by_data_source_id(data_source_id):
    return requests.get(BASE_URL + f"{tenant_id}/{api_id}/filter/{data_source_id}", headers=TOKEN)

def create_business_logic():
    random_number = get_unique_int_number()
    payload = {
        "Name": f"Business Logic Created by Pytest - {random_number}",
        "Description":"Add Modified By",
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
    return requests.post(BASE_URL + f"{tenant_id}/{api_id}/logic", headers=TOKEN, json=payload)

def get_business_logic(test_business_logic_id):
    return requests.get(BASE_URL + f"{tenant_id}/{api_id}/logic/{test_business_logic_id}", headers=TOKEN)

def create_database_connection():
    payload = {
        "DBType":"postgres",
        "Host":"10.10.16.201",
        "Login":"postgres",
        "Description":"db connection for pytest",
        "Name":"nextapi-test",
        "Port":4041,
        "Password":"{{SECRET:NEXTAPI_DEV_DB_PASSWORD}}",
        "DBName":"demo",
        "LowerCaseColumns":[],
        "UseUpperCaseColumnNames":True
    }
    return requests.post(BASE_URL + f"{tenant_id}/{api_id}/database/connection/", headers=TOKEN, json=payload)

def get_database_connection(connection_id):
    return requests.get(BASE_URL + f"{tenant_id}/{api_id}/database/connection/{connection_id}", headers=TOKEN)

def get_database_by_id(database_id):
    return requests.get(BASE_URL + f"{tenant_id}/{api_id}/database/datasource/{database_id}", headers=TOKEN)

def create_database():
    random_number = get_unique_int_number()
    params = {"env": 20}
    payload = {
        "Name":f"Create Database by Pytest - {random_number}",
        "SQLType":"table",
        "SQL":"public.demo_uuid",
        "ConnectionID": int(connection_id),
        "Operations":[{"Operation":"select"}],
        "GenerateEndpoints":False,
        "Details":[
            {
                "Alias":"",
                "Name":"id",
                "DataType":"integer",
                "ItemType":"",
                "Length":32,
                "Nullable":False,
                "PrimaryKey":True,
                "AutoIncrement":False,
                "Type":"column",
                "Mapping":{
                    "input":{
                        "grpc_message":["id"],
                        "array_marker":["id"]
                    },
                    "output":{
                        "grpc_message":["id"],
                        "array_marker":["id"]
                    }
                },
                "No":1
            }
        ]
    }
    return requests.post(BASE_URL + f"{tenant_id}/{api_id}/database/datasource/{connection_id}", headers=TOKEN, params=params, json=payload)

def create_business_rule():
    random_number = get_unique_int_number()
    payload = {
        "Name": f"Pytest Business Rule - {random_number}",
        "Description":"Business Rule Created by Pytest",
        "DMNID": dmn_id,
        "Details":[
            {
                "FilterID":0,
                "Name":"",
                "Label":"age",
                "Type":"input",
                "DataType":"int32",
                "MappingType":"grpc_message",
                "Value":[]
            },
            {
                "FilterID":0,
                "Name":"category",
                "Label":"category",
                "Type":"output",
                "DataType":"string",
                "MappingType":"grpc_message",
                "Value":["category"]
            }
        ]
    }
    return requests.post(BASE_URL + f"{tenant_id}/{api_id}/dmn/filter", headers=TOKEN, json=payload)

def get_business_rule(business_rule_id):
    return requests.get(BASE_URL + f"{tenant_id}/{api_id}/dmn/filter/{business_rule_id}", headers=TOKEN)

def get_ddl_database(test_connection_id):
    params = {"env": 20}
    database_name = "public.demo_uuid"
    return requests.get(BASE_URL + f"{tenant_id}/{api_id}/database/ddl-table/{test_connection_id}/{database_name}", headers=TOKEN, params=params)
    
def create_api_by_data_source(input_data_source=None):
    number = get_unique_int_number()
    if input_data_source is None:
        url_data_source = data_source
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
    elif input_data_source == "nextbytes_send_email":
        url_data_source = nextbytes_data_source
        payload = {
            "Name": f"Pytest Send Email - {number}",
            "Type": "next_bytes",
            "Description": "Send Email Created by Pytest",
            "Specification": {
                "url": {
                "constant": "https://nextmail-api.cloud.nextplatform.ai/api/transactionals/",
                "type": "string"
                },
                "template_id": {
                "constant": "20",
                "type": "string"
                },
                "bearer_token": {
                "constant": "",
                "type": "string"
                },
                "api_key": {
                "constant": "1a97a681-1563-4d18-b965-110ff95c8564:YZonYRiBrDnNgcijzeb58Cp6vcuUOKlU",
                "type": "string"
                },
                "recipients": {
                "grpc_message": [
                    "recipients"
                ],
                "type": "string",
                "array_marker": [
                    "*"
                ]
                },
                "attribs": [
                {
                    "from": {
                    "grpc_message": [
                        "email"
                    ]
                    },
                    "to": {
                    "nextbytes": "email"
                    },
                    "array_marker": [
                    "email"
                    ],
                    "type": "string"
                },
                {
                    "from": {
                    "grpc_message": [
                        "password"
                    ]
                    },
                    "to": {
                    "nextbytes": "password"
                    },
                    "type": "string",
                    "array_marker": [
                    "password"
                    ]
                }
                ],
                "attribs_detail": []
            }
        }
    elif input_data_source == "nextbytes_doc_generator":
        url_data_source = nextbytes_doc_generator_data_source
        payload = {
            "Name": f"Pytest Generate Document - {number}",
            "Type": "document_generator",
            "Description": "Generate Document Created by Pytest",
            "Specification": {
                "baseUrl": {
                "constant": "https://nextmail-api.cloud.nextplatform.ai/api",
                "type": "string"
                },
                "template_id": {
                "constant": "8",
                "type": "string"
                },
                "bearer_token": {
                "constant": "",
                "type": "string"
                },
                "api_key": {
                "constant": "1a97a681-1563-4d18-b965-110ff95c8564:YZonYRiBrDnNgcijzeb58Cp6vcuUOKlU",
                "type": "string"
                },
                "document_type": {
                "constant": "pdf",
                "type": "string"
                },
                "content_type": {
                "grpc_message": [
                    "content_type"
                ],
                "type": "string",
                "array_marker": [
                    "content_type"
                ]
                },
                "content": {
                "grpc_message": [
                    "data"
                ],
                "type": "bytes",
                "array_marker": [
                    "data"
                ]
                },
                "download_file": True,
                "mapping": [
                {
                    "from": {
                    "grpc_message": [
                        "wil_bpd"
                    ]
                    },
                    "to": [
                    "wil_bpd"
                    ],
                    "array_marker": [
                    "wil_bpd"
                    ],
                    "type": "string"
                },
                {
                    "from": {
                    "grpc_message": [
                        "bulan"
                    ]
                    },
                    "to": [
                    "bulan"
                    ],
                    "array_marker": [
                    "bulan"
                    ],
                    "type": "string"
                },
                {
                    "from": {
                    "grpc_message": [
                        "thn_anggaran"
                    ]
                    },
                    "to": [
                    "thn_anggaran"
                    ],
                    "array_marker": [
                    "thn_anggaran"
                    ],
                    "type": "string"
                },
                {
                    "from": {
                    "grpc_message": [
                        "penerimaan_penyetoran"
                    ]
                    },
                    "to": [
                    "penerimaan_penyetoran"
                    ],
                    "array_marker": [
                    "penerimaan_penyetoran"
                    ],
                    "type": "string"
                }
                ],
                "template": {
                "wil_bpd": "JAKARTA SELATAN",
                "bulan": "OKTOBER",
                "thn_anggaran": "I",
                "penerimaan_penyetoran": [
                    {
                    "no": "1",
                    "no_rekening": "1230001",
                    "jenis_pungutan": "PKB",
                    "sisa_setor": "Rp 1.000.000",
                    "ket": "belum lunas",
                    "penerimaan": {
                        "sd_bulan_lalu": "Rp 57.000.000",
                        "bulan_ini": "Rp 7.000.000",
                        "sd_bulan_ini": "Rp 64.000.000"
                    },
                    "penyetoran": {
                        "sd_bulan_lalu": "Rp 57.000.000",
                        "bulan_ini": "Rp 8.000.000",
                        "sd_bulan_ini": "Rp 64.000.000"
                    }
                    }
                ]
                },
                "mapping_detail": [
                {
                    "array_marker": [
                    "wil_bpd"
                    ],
                    "from": {
                    "grpc_message": [
                        "wil_bpd"
                    ]
                    },
                    "type": "string"
                },
                {
                    "array_marker": [
                    "bulan"
                    ],
                    "from": {
                    "grpc_message": [
                        "bulan"
                    ]
                    },
                    "type": "string"
                },
                {
                    "array_marker": [
                    "thn_anggaran"
                    ],
                    "from": {
                    "grpc_message": [
                        "thn_anggaran"
                    ]
                    },
                    "type": "string"
                },
                {
                    "array_marker": [
                    "*",
                    "no"
                    ],
                    "from": {
                    "grpc_message": [
                        "penerimaan_penyetoran",
                        "no"
                    ]
                    },
                    "type": "string"
                },
                {
                    "array_marker": [
                    "*",
                    "no_rekening"
                    ],
                    "from": {
                    "grpc_message": [
                        "penerimaan_penyetoran",
                        "no_rekening"
                    ]
                    },
                    "type": "string"
                },
                {
                    "array_marker": [
                    "*",
                    "jenis_pungutan"
                    ],
                    "from": {
                    "grpc_message": [
                        "penerimaan_penyetoran",
                        "jenis_pungutan"
                    ]
                    },
                    "type": "string"
                },
                {
                    "array_marker": [
                    "*",
                    "sisa_setor"
                    ],
                    "from": {
                    "grpc_message": [
                        "penerimaan_penyetoran",
                        "sisa_setor"
                    ]
                    },
                    "type": "string"
                },
                {
                    "array_marker": [
                    "*",
                    "ket"
                    ],
                    "from": {
                    "grpc_message": [
                        "penerimaan_penyetoran",
                        "ket"
                    ]
                    },
                    "type": "string"
                },
                {
                    "array_marker": [
                    "*",
                    "penerimaan",
                    "sd_bulan_lalu"
                    ],
                    "from": {
                    "grpc_message": [
                        "penerimaan_penyetoran",
                        "penerimaan",
                        "sd_bulan_lalu"
                    ]
                    },
                    "type": "string"
                },
                {
                    "array_marker": [
                    "*",
                    "penerimaan",
                    "bulan_ini"
                    ],
                    "from": {
                    "grpc_message": [
                        "penerimaan_penyetoran",
                        "penerimaan",
                        "bulan_ini"
                    ]
                    },
                    "type": "string"
                },
                {
                    "array_marker": [
                    "*",
                    "penerimaan",
                    "sd_bulan_ini"
                    ],
                    "from": {
                    "grpc_message": [
                        "penerimaan_penyetoran",
                        "penerimaan",
                        "sd_bulan_ini"
                    ]
                    },
                    "type": "string"
                },
                {
                    "array_marker": [
                    "*",
                    "penyetoran",
                    "sd_bulan_lalu"
                    ],
                    "from": {
                    "grpc_message": [
                        "penerimaan_penyetoran",
                        "penyetoran",
                        "sd_bulan_lalu"
                    ]
                    },
                    "type": "string"
                },
                {
                    "array_marker": [
                    "*",
                    "penyetoran",
                    "bulan_ini"
                    ],
                    "from": {
                    "grpc_message": [
                        "penerimaan_penyetoran",
                        "penyetoran",
                        "bulan_ini"
                    ]
                    },
                    "type": "string"
                },
                {
                    "array_marker": [
                    "*",
                    "penyetoran",
                    "sd_bulan_ini"
                    ],
                    "from": {
                    "grpc_message": [
                        "penerimaan_penyetoran",
                        "penyetoran",
                        "sd_bulan_ini"
                    ]
                    },
                    "type": "string"
                }
                ]
            }
        }
    elif input_data_source == "arangodb":
        url_data_source = arangodb_data_source
        payload = {
            "Name": f"Pytest ArangoDB - {number}",
            "Type": "arangodb_data_source",
            "Description": "ArangoDB Created by Pytest",
            "Specification": {
                "server": "https://arangodb.dcnlink.com",
                "database": "flights",
                "username": "root",
                "password": "{{SECRET:LOCAL_ARANGO_DB_PASS}}",
                "input": [
                {
                    "from": {
                    "constant": "Papua New Guinea"
                    },
                    "to": "country",
                    "type": "string",
                    "array_marker": [
                    "country"
                    ]
                }
                ],
                "output": [
                {
                    "from": [],
                    "to": {
                    "grpc_message": [
                        "output"
                    ]
                    },
                    "type": "object",
                    "array_marker": [
                    "*"
                    ]
                }
                ],
                "outputExample": [
                {
                    "IATA": "PX",
                    "ICAO": "ANG",
                    "_id": "airlines/328",
                    "_key": "328",
                    "_rev": "_foEERm2---",
                    "alias": "\\N",
                    "callsign": "NUIGINI",
                    "country": "Papua New Guinea",
                    "name": "Air Niugini"
                },
                {
                    "IATA": "CG",
                    "ICAO": "TOK",
                    "_id": "airlines/1308",
                    "_key": "1308",
                    "_rev": "_foEE5WW---",
                    "alias": "\\N",
                    "callsign": "BALUS",
                    "country": "Papua New Guinea",
                    "name": "Airlines PNG"
                },
                {
                    "IATA": "CN",
                    "ICAO": "",
                    "_id": "airlines/2946",
                    "_key": "2946",
                    "_rev": "_foEF3oS---",
                    "alias": "\\N",
                    "callsign": "",
                    "country": "Papua New Guinea",
                    "name": "Islands Nationair"
                },
                {
                    "IATA": "N9",
                    "ICAO": "",
                    "_id": "airlines/3701",
                    "_key": "3701",
                    "_rev": "_foEGL3G---",
                    "alias": "\\N",
                    "callsign": "",
                    "country": "Papua New Guinea",
                    "name": "North Coast Aviation"
                },
                {
                    "IATA": "",
                    "ICAO": "TAL",
                    "_id": "airlines/4866",
                    "_key": "4866",
                    "_rev": "_foEGuJa---",
                    "alias": "\\N",
                    "callsign": "TALAIR",
                    "country": "Papua New Guinea",
                    "name": "Talair"
                }
                ],
                "output_detail": [
                {
                    "array_marker": [
                    "*",
                    "IATA"
                    ],
                    "to": {
                    "grpc_message": [
                        "output",
                        "IATA"
                    ]
                    },
                    "type": "string"
                },
                {
                    "array_marker": [
                    "*",
                    "ICAO"
                    ],
                    "to": {
                    "grpc_message": [
                        "output",
                        "ICAO"
                    ]
                    },
                    "type": "string"
                },
                {
                    "array_marker": [
                    "*",
                    "_id"
                    ],
                    "to": {
                    "grpc_message": [
                        "output",
                        "_id"
                    ]
                    },
                    "type": "string"
                },
                {
                    "array_marker": [
                    "*",
                    "_key"
                    ],
                    "to": {
                    "grpc_message": [
                        "output",
                        "_key"
                    ]
                    },
                    "type": "string"
                },
                {
                    "array_marker": [
                    "*",
                    "_rev"
                    ],
                    "to": {
                    "grpc_message": [
                        "output",
                        "_rev"
                    ]
                    },
                    "type": "string"
                },
                {
                    "array_marker": [
                    "*",
                    "alias"
                    ],
                    "to": {
                    "grpc_message": [
                        "output",
                        "alias"
                    ]
                    },
                    "type": "string"
                },
                {
                    "array_marker": [
                    "*",
                    "callsign"
                    ],
                    "to": {
                    "grpc_message": [
                        "output",
                        "callsign"
                    ]
                    },
                    "type": "string"
                },
                {
                    "array_marker": [
                    "*",
                    "country"
                    ],
                    "to": {
                    "grpc_message": [
                        "output",
                        "country"
                    ]
                    },
                    "type": "string"
                },
                {
                    "array_marker": [
                    "*",
                    "name"
                    ],
                    "to": {
                    "grpc_message": [
                        "output",
                        "name"
                    ]
                    },
                    "type": "string"
                }
            ],
                "query": "for a in airlines filter a.country == @country limit 5 return a"
            }
        }
    elif input_data_source == "soap":
        url_data_source = soap_data_source
        payload = {
            "Name": f"Pytest SOAP - {number}",
            "Type": "soap_data_source",
            "Description": "SOAP Created by Pytest",
            "Specification": {
                "PortType": "NumberConversionSoapType",
                "WsdlUrl": "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL",
                "Mode": "url",
                "File": "",
                "WsdlPath": "",
                "WsdlMain": "wsdl.wsdl",
                "wsdl": "wsdl.wsdl",
                "operation": "NumberToDollars",
                "input": [
                {
                    "from": {
                    "grpc_message": [
                        "ubi_num"
                    ]
                    },
                    "to": {
                    "soap": {
                        "path": [
                        "ubiNum"
                        ],
                        "messagePart": "parameters"
                    }
                    },
                    "rowData": {
                    "Operation": "NumberToWords",
                    "OperationID": "0",
                    "Msg": "NumberToWordsSoapRequest",
                    "MsgPart": "parameters",
                    "MsgPartID": 0,
                    "Path": "ubiNum",
                    "PathID": 0,
                    "RawPath": "ubiNum",
                    "Type": "unsignedLong",
                    "Name": "ubi_num",
                    "ID": 1,
                    "IsHeader": False,
                    "RepeatedFields": []
                    }
                },
                {
                    "from": {
                    "grpc_message": [
                        "d_num"
                    ]
                    },
                    "to": {
                    "soap": {
                        "path": [
                        "dNum"
                        ],
                        "messagePart": "parameters"
                    }
                    },
                    "rowData": {
                    "Operation": "NumberToDollars",
                    "OperationID": "1",
                    "Msg": "NumberToDollarsSoapRequest",
                    "MsgPart": "parameters",
                    "MsgPartID": 0,
                    "Path": "dNum",
                    "PathID": 0,
                    "RawPath": "dNum",
                    "Type": "decimal",
                    "Name": "d_num",
                    "ID": 2,
                    "IsHeader": False,
                    "RepeatedFields": []
                    }
                }
                ],
                "output": [
                {
                    "to": {
                    "grpc_message": [
                        "number_to_words_result"
                    ]
                    },
                    "from": {
                    "soap": {
                        "path": [
                        "NumberToWordsResult"
                        ],
                        "messagePart": "parameters"
                    }
                    },
                    "rowData": {
                    "Operation": "NumberToWords",
                    "OperationID": "0",
                    "Msg": "NumberToWordsSoapResponse",
                    "MsgPart": "parameters",
                    "MsgPartID": 0,
                    "Path": "NumberToWordsResult",
                    "PathID": 0,
                    "RawPath": "NumberToWordsResult",
                    "Type": "string",
                    "Name": "number_to_words_result",
                    "ID": 1,
                    "IsHeader": False,
                    "RepeatedFields": []
                    }
                },
                {
                    "to": {
                    "grpc_message": [
                        "number_to_dollars_result"
                    ]
                    },
                    "from": {
                    "soap": {
                        "path": [
                        "NumberToDollarsResult"
                        ],
                        "messagePart": "parameters"
                    }
                    },
                    "rowData": {
                    "Operation": "NumberToDollars",
                    "OperationID": "1",
                    "Msg": "NumberToDollarsSoapResponse",
                    "MsgPart": "parameters",
                    "MsgPartID": 0,
                    "Path": "NumberToDollarsResult",
                    "PathID": 0,
                    "RawPath": "NumberToDollarsResult",
                    "Type": "string",
                    "Name": "number_to_dollars_result",
                    "ID": 2,
                    "IsHeader": False,
                    "RepeatedFields": []
                    }
                }
            ]
            },
            "Files": [
                {
                "Name": "wsdl.wsdl",
                "DownloadURL": "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"
                }
            ]
        }
    elif input_data_source == "faas":
        url_data_source = faas_data_source
        payload = {
            "Name": f"Pytest Custom Function - {number}",
            "Type":"faas",
            "Description":"Custom Function created by Pytest",
            "Specification":{
                "address":"https://fission.lab.nextplatform.ai/lab/greeting",
                "host":"",
                "engine":"fission",
                "function":"Greeting",
                "language":"nodejs",
                "json_input":[
                    {
                        "from":{
                            "grpc_message":["name"]
                        },
                        "to":{
                            "json":["name"]
                        },
                        "type":"string",
                        "array_marker":[""]
                    }
                ],
                "json_output":[
                    {
                        "to":{
                            "grpc_message":["msg"]
                        },
                        "from":{
                            "json":["msg"]
                        },
                        "type":"string",
                        "array_marker":[""]
                    }
                ]
            }
        }
    elif input_data_source == "nextflow":
        url_data_source = nextflow_data_source
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
    return requests.post(BASE_URL + f"{tenant_id}/{api_id}/filter/{url_data_source}", headers=TOKEN, json=payload)