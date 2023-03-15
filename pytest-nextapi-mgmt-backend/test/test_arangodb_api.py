import requests
import json
from helper import create_endpoint, get_endpoint_by_id, get_token, get_tenant_id, get_api_id, get_base_url, get_data_source, get_unique_int_number, create_api_by_data_source, get_api_by_data_source_id

BASE_URL = get_base_url()
tenant_id = get_tenant_id()
TOKEN = get_token()
api_id = get_api_id()
data_source = get_data_source("arangodb")

def test_get_arangodb_api_by_data_source():
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

def test_get_query_result_arangodb():
    params = {"env": 20}
    payload = {
        "Name":"Pytest ArangoDB",
        "Description":"ArangoDB Created by Pytest",
        "server":"https://arangodb.dcnlink.com",
        "database":"flights",
        "username":"root",
        "password":"{{SECRET:LOCAL_ARANGO_DB_PASS}}",
        "InputMappingEditor":{"parameters":[]},
        "OutputMappingEditor":{"parameters":[]},
        "query":"for a in airlines filter a.country == @country limit 5 return a",
        "params":{
            "country":"Papua New Guinea"
        }
    }
    response =  requests.post(BASE_URL + f"{tenant_id}/{api_id}/arango", headers=TOKEN, params=params, json=payload)
    assert response.status_code == 200

    data = response.json()
    # print(data)
    assert len(data) >= 0

def test_create_arangodb_api_by_data_source():
    number = get_unique_int_number()
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
    response = requests.post(BASE_URL + f"{tenant_id}/{api_id}/filter/{data_source}", headers=TOKEN, json=payload)
    assert response.status_code == 200

    data = response.json()
    # print(data)
    # API_ID_data = data["APIID"]
    assert data["APIID"] == int(api_id)
    assert data["Name"] == f"Pytest ArangoDB - {number}"

def test_edit_arangodb_api_by_data_source():
    create_api = create_api_by_data_source("arangodb")
    assert create_api.status_code == 200
    
    create_api_data = create_api.json()
    create_api_name = create_api_data["Name"]
    create_api_id = create_api_data["ID"]

    payload = {
        "Name": create_api_name,
        "Type": "arangodb_data_source",
        "Description": "ArangoDB Created and Edited by Pytest",
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
    response = requests.put(BASE_URL + f"{tenant_id}/{api_id}/filter/{data_source}/{create_api_id}", headers=TOKEN, json=payload)
    # update_data = response.json()
    # print(update_data)
    assert response.status_code == 200

    test_get_api = get_api_by_data_source_id(create_api_id)
    assert test_get_api.status_code == 200
    test_get_api_data = test_get_api.json()
    test_get_api_desc = test_get_api_data["Description"]
    assert test_get_api_desc == "ArangoDB Created and Edited by Pytest"

def test_delete_arangodb_api_by_data_source_id():
    create_api = create_api_by_data_source("arangodb")
    assert create_api.status_code == 200
    
    create_api_data = create_api.json()
    create_api_id = create_api_data["ID"]

    response = requests.delete(BASE_URL + f"{tenant_id}/{api_id}/filter/{create_api_id}", headers=TOKEN)
    assert response.status_code == 200

    test_get_api = get_api_by_data_source_id(create_api_id)
    test_get_api_data = test_get_api.json()
    assert test_get_api.status_code == 400
    assert test_get_api_data["detail"] == f"query Filter Definition ID {create_api_id} failed: record not found"

def test_update_arangodb_endpoint():
    create_api = create_api_by_data_source("arangodb")
    assert create_api.status_code == 200
    
    create_api_data = create_api.json()
    create_api_name = create_api_data["Name"]
    create_api_id = create_api_data["ID"]
    create_api_global_id = create_api_data["GlobalID"]

    test_create_endpoint = create_endpoint("arangodb")
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
            "Type": "arangodb_data_source",
            "Summary": "ArangoDB Created by Pytest",
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
                "query": "for a in airlines filter a.country == @country limit 5 return a",
                "id": create_api_global_id
            },
            "EndpointID": int(test_create_endpoint_id)
            }
        ]
    }
    update_pipeline = requests.put(BASE_URL + f"{tenant_id}/{test_create_endpoint_id}/pipelines/", headers=TOKEN, json=update_pipeline_payload)
    assert update_pipeline.status_code == 200

    edit_arangodb_payload = {
        "Name": create_api_name,
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
                "grpc_message": [
                    "country"
                ]
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
    update_arangodb = requests.put(BASE_URL + f"{tenant_id}/{api_id}/filter/{data_source}/{create_api_id}", headers=TOKEN, json=edit_arangodb_payload)
    assert update_arangodb.status_code == 200

    update_endpoint_arangodb_payload = {
        "Endp": [
            int(test_create_endpoint_id)
        ],
        "Spec": {
            "server": "https://arangodb.dcnlink.com",
            "database": "flights",
            "username": "root",
            "password": "{{SECRET:LOCAL_ARANGO_DB_PASS}}",
            "input": [
            {
                "from": {
                "grpc_message": [
                    "country"
                ]
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
            "query": "for a in airlines filter a.country == @country limit 5 return a",
            "id": create_api_global_id
        }
        }
    update_arangodb = requests.post(BASE_URL + f"{tenant_id}/{api_id}/filter/updatefilter/{data_source}/{create_api_id}", headers=TOKEN, json=update_endpoint_arangodb_payload)
    update_arangodb_data = update_arangodb.json()
    # print(update_arangodb_data)
    assert update_arangodb.status_code == 200
    assert update_arangodb_data["status"] == "succes"
    
    