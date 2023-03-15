import requests
import json
from helper import get_base_url, get_tenant_id, get_token, get_api_id, get_endpoint_id, get_unique_int_number, get_endpoint_by_id, create_endpoint, get_data_source, get_data_source_id, create_api_by_data_source, get_api_by_data_source_id

BASE_URL = get_base_url()
TOKEN = get_token()
tenant_id = get_tenant_id()
api_id = get_api_id()
data_source = get_data_source()

def test_can_get_list_endpoint():
    response = requests.get(BASE_URL + f"{tenant_id}/{api_id}/endpoint/", headers=TOKEN)
    assert response.status_code == 200

    data = response.json()
    assert len(data) >= 0

def test_get_endpoint():
    endpoint_id = get_endpoint_id()
    response = requests.get(BASE_URL + f"{tenant_id}/{api_id}/endpoint/{endpoint_id}", headers=TOKEN)
    assert response.status_code == 200

    get_endpoint_data = response.json()
    assert get_endpoint_data["Name"] == "Get Account"

def test_get_params():
    endpoint_id = get_endpoint_id()
    response = requests.get(BASE_URL + f"{tenant_id}/{api_id}/endpoint/{endpoint_id}/params", headers=TOKEN)
    assert response.status_code == 200

    get_params_data = response.json()
    assert get_params_data["Services"][0]["Name"] == "Apiforpytestv10"

def test_get_endpoint_grid():
    payload = {
        "take":10,
        "skip":0,
        "page":1,
        "pageSize":10,
        "sort": [
            {
            "field":"name",
            "dir":"asc"
            }
        ],
        "group":[]
    }
    response = requests.post(BASE_URL + f"{tenant_id}/{api_id}/endpoint-grid", headers=TOKEN, json=payload)
   # print(BASE_URL + f"{tenant_id}/api-grid")
    assert response.status_code == 200

    data = response.json()
    # print(data)
    assert len(data["data"]) >= 0

def test_create_endpoint():
    random_number = get_unique_int_number()
    payload = {
        "Type":"custom",
        "Name": f"Pytest Create Endpoint - {random_number}",
        "Summary":"Endpoint created by pytest",
        "ResourceName":"",
        "RESTMethod":"",
        "LogLevel":""
    }

    response = requests.post(BASE_URL + f"{tenant_id}/{api_id}/endpoint", headers=TOKEN, json=payload)
   # print(BASE_URL + f"{tenant_id}/api-grid")
    assert response.status_code == 200

    data = response.json()
    endpoint_id = data["ID"]
    endpoint_name = data["Name"]

    test_get_endpoint_resp = get_endpoint_by_id(endpoint_id)
    assert test_get_endpoint_resp.status_code == 200

    test_get_endpoint_data = test_get_endpoint_resp.json()
    test_get_endpoint_name = test_get_endpoint_data["Name"]
    assert test_get_endpoint_name == endpoint_name

def test_edit_endpoint():
    create_endpoint_resp = create_endpoint()
    assert create_endpoint_resp.status_code == 200
    
    create_endpoint_data = create_endpoint_resp.json()
    create_endpoint_id = create_endpoint_data["ID"]
    create_endpoint_name = create_endpoint_data["Name"]

    payload = {
        "ID": create_endpoint_id,
        "Name": create_endpoint_name,
        "Summary": "Endpoint created and edited by pytest",
        "ResourceName":"",
        "RESTMethod":"",
        "LogLevel":""
    }
    response = requests.put(BASE_URL + f"{tenant_id}/{api_id}/endpoint/{create_endpoint_id}", headers=TOKEN, json=payload)
    assert response.status_code == 200

    # edited_data = response.json()
    # edited_data_summary = edited_data["Summary"]

    test_get_endpoint = get_endpoint_by_id(create_endpoint_id)
    assert test_get_endpoint.status_code == 200
    test_get_endpoint_data = test_get_endpoint.json()
    test_get_endpoint_data_summary = test_get_endpoint_data["Summary"]

    assert test_get_endpoint_data_summary == "Endpoint created and edited by pytest"

def test_delete_endpoint():
    create_endpoint_resp = create_endpoint()
    assert create_endpoint_resp.status_code == 200
    
    create_endpoint_data = create_endpoint_resp.json()
    create_endpoint_id = create_endpoint_data["ID"]

    response = requests.delete(BASE_URL + f"{tenant_id}/{api_id}/endpoint/{create_endpoint_id}", headers=TOKEN)
    assert response.status_code == 200

    test_get_endpoint = get_endpoint_by_id(create_endpoint_id)
    test_get_endpoint_data = test_get_endpoint.json()
    assert test_get_endpoint.status_code == 400
    assert test_get_endpoint_data["detail"] == "query endpoint detail failed: record not found"