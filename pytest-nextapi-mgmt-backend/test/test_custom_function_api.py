import requests
import json
from helper import get_tenant_id, get_token, get_api_id, get_unique_int_number, get_data_source, create_api_by_data_source, get_api_by_data_source_id, get_base_url

BASE_URL = get_base_url()
CUSTOM_FUNCTION_URL = get_base_url("custom_function")
api_id = get_api_id()
data_source = get_data_source("faas")
TOKEN = get_token()
tenant_id = get_tenant_id()


def test_get_faas_api_by_data_source():
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

def test_create_faas_api_by_data_source():
    number = get_unique_int_number()
    payload = {
        "Name": f"Pytest Custom Function - {number}",
        "Type":"faas",
        "Description":"Custom Function Created by Pytest",
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
    response = requests.post(BASE_URL + f"{tenant_id}/{api_id}/filter/{data_source}", headers=TOKEN, json=payload)
    assert response.status_code == 200

    data = response.json()
    # print(data)
    API_ID_data = data["APIID"]
    assert API_ID_data == int(api_id)

def test_edit_faas_api_by_data_source():
    create_api = create_api_by_data_source("faas")
    assert create_api.status_code == 200
    
    create_api_data = create_api.json()
    create_api_name = create_api_data["Name"]
    create_api_id = create_api_data["ID"]

    payload = {
        "Name": create_api_name,
        "Type":"faas",
        "Description":"Custom Function Created and Edited by Pytest",
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
    response = requests.put(BASE_URL + f"{tenant_id}/{api_id}/filter/{data_source}/{create_api_id}", headers=TOKEN, json=payload)
    update_data = response.json()
    assert response.status_code == 200

    test_get_api = get_api_by_data_source_id(create_api_id)
    assert test_get_api.status_code == 200
    test_get_api_data = test_get_api.json()
    test_get_api_desc = test_get_api_data["Description"]
    assert test_get_api_desc == "Custom Function Created and Edited by Pytest"

def test_delete_faas_api_by_data_source_id():
    create_api = create_api_by_data_source("faas")
    assert create_api.status_code == 200
    
    create_api_data = create_api.json()
    create_api_id = create_api_data["ID"]

    response = requests.delete(BASE_URL + f"{tenant_id}/{api_id}/filter/{create_api_id}", headers=TOKEN)
    assert response.status_code == 200

    test_get_api = get_api_by_data_source_id(create_api_id)
    test_get_api_data = test_get_api.json()
    assert test_get_api.status_code == 400
    assert test_get_api_data["detail"] == f"query Filter Definition ID {create_api_id} failed: record not found"

def test_get_list_function():
    payload = {
        "take":5,
        "skip":0,
        "page":1,
        "pageSize":5,
        "group":[]
    }
    response = requests.post(CUSTOM_FUNCTION_URL + f"{tenant_id}/func/grid", headers=TOKEN, json=payload)
    # data = response.json()
    # print(data)
    assert response.status_code == 200

    data = response.json()
    # print(data)
    assert len(data["data"]) >= 0
