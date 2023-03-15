import requests
import json
from helper import get_base_url, get_token, get_tenant_id, get_api_id, get_unique_int_number, get_dmn_id, create_business_rule, get_business_rule

BASE_URL = get_base_url()
BUSINESS_RULE_URL = get_base_url("business_rule")
tenant_id = get_tenant_id()
TOKEN = get_token()
api_id = get_api_id()
dmn_id = get_dmn_id()
business_rule_id = "92"

def test_get_business_rule_list():
    payload = {
        "take":10,
        "skip":0,
        "page":1,
        "pageSize":10,
        "group":[]
    }
    response =  requests.post(BASE_URL + f"{tenant_id}/{api_id}/dmn/filter-grid", headers=TOKEN, json=payload)
    # data = response.json()
    # print(data)
    assert response.status_code == 200

    data = response.json()
    # print(data)
    assert data["total"] >= 0

def test_get_business_rule_mapping():
    payload = dmn_id
    response =  requests.post(BASE_URL + f"{tenant_id}/{api_id}/dmn/mapping", headers=TOKEN, data=payload)
    # data = response.json()
    # print(data)
    assert response.status_code == 200

    data = response.json()
    # print(data)
    assert len(data) > 0
    assert data[1]["Name"] == 'category'

def test_create_business_rule():
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
    response = requests.post(BASE_URL + f"{tenant_id}/{api_id}/dmn/filter", headers=TOKEN, json=payload)
    assert response.status_code == 200

    data = response.json()
    assert data["DMNID"] == dmn_id

def test_get_business_rule():
    response = requests.get(BASE_URL + f"{tenant_id}/{api_id}/dmn/filter/{business_rule_id}", headers=TOKEN)
    # data = response.json()
    # print(data)
    assert response.status_code == 200

    data = response.json()
    # print(data)
    assert data["DMNID"] == dmn_id

def test_delete_business_rule():
    test_create_business_rule = create_business_rule()
    assert test_create_business_rule.status_code == 200
    test_create_business_rule_data = test_create_business_rule.json()
    test_create_business_rule_id = test_create_business_rule_data["ID"]

    response = requests.delete(BASE_URL + f"{tenant_id}/{api_id}/dmn/filter/{test_create_business_rule_id}", headers=TOKEN)
    assert response.status_code == 200

    test_get_business_rule = get_business_rule(test_create_business_rule_id)
    test_get_business_rule_data = test_get_business_rule.json()
    # print(test_get_business_rule_data)
    assert test_get_business_rule.status_code == 400
    assert test_get_business_rule_data["detail"] == f"query DMN Filter Definition ID {test_create_business_rule_id} failed: record not found"

def test_edit_business_rule():
    test_create_business_rule = create_business_rule()
    assert test_create_business_rule.status_code == 200
    test_create_business_rule_data = test_create_business_rule.json()
    test_create_business_rule_id = test_create_business_rule_data["ID"]
    test_create_business_rule_name = test_create_business_rule_data["Name"]

    payload = payload = {
        "Name": test_create_business_rule_name,
        "Description":"Business Rule Created and Edited by Pytest",
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
    response = requests.put(BASE_URL + f"{tenant_id}/{api_id}/dmn/filter/{test_create_business_rule_id}", headers=TOKEN, json=payload)
    assert response.status_code == 200

    test_get_business_rule = get_business_rule(test_create_business_rule_id)
    test_get_business_rule_data = test_get_business_rule.json()
    # print(test_get_business_rule_data)
    assert test_get_business_rule.status_code == 200
    assert test_get_business_rule_data["Description"] == "Business Rule Created and Edited by Pytest"

def test_get_list_business_rule():
    payload = {
        "take":10,
        "skip":0,
        "page":1,
        "pageSize":10,
        "group":[]
    }
    response = requests.post(BUSINESS_RULE_URL + f"{tenant_id}/files-grid", headers=TOKEN, json=payload)
    # data = response.json()
    # print(data)
    assert response.status_code == 200

    data = response.json()
    # print(data)
    assert len(data["data"]) >= 0