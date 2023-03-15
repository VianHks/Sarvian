import requests
import json
from helper import get_token, get_tenant_id, get_api_id, get_unique_int_number, get_api_by_id, get_base_url

BASE_URL = get_base_url()
TOKEN = get_token()
tenant_id = get_tenant_id()
api_id = get_api_id()
env_id = 20

def test_can_get_list_api():
    response = requests.get(BASE_URL + f"{tenant_id}/api/", headers=TOKEN)
    assert response.status_code == 200

    data = response.json()
    assert len(data) >= 0

#masih 500
# def test_can_get_list_running_api():
#     response = requests.get(BASE_URL + f"{tenant_id}/api/running", headers=TOKEN)
#     assert response.status_code == 200

#     data = response.json()
#     assert len(data) >= 0

def test_can_get_list_search_api():
    response = requests.get(BASE_URL + f"{tenant_id}/api/search", headers=TOKEN)
    assert response.status_code == 200

    data = response.json()
    # print(data[0])
    assert len(data) >= 0

def test_get_api():
    response = requests.get(BASE_URL + f"{tenant_id}/api/{api_id}", headers=TOKEN)
    assert response.status_code == 200

    data = response.json()
    assert data["Name"] == "API for Pytest"

def test_get_env_cluster():
    response = requests.get(BASE_URL + f"{tenant_id}/env/cluster", headers=TOKEN)
    assert response.status_code == 200

    data = response.json()
    print(data["body"])
    assert data["body"][0]["id"] == 20

def test_get_env_variable():
    response = requests.get(BASE_URL + f"{tenant_id}/env/{env_id}/variable", headers=TOKEN)
    # print(data)
    assert response.status_code == 200

    data = response.json()
    assert data[0]["ID"] == 55

def test_get_running_api_env():
    response = requests.get(BASE_URL + f"{tenant_id}/api-running/{env_id}", headers=TOKEN)
    # print(data)
    assert response.status_code == 200

    data = response.json()
    assert len(data) >= 0

def test_get_api_grid():
    payload = {
        "skip":30,
        "page":6,
        "pageSize":6,
        "filter":{
            "logic":"and",
            "filters":[]
        },
        "sort":[
            {
            "field":"created_at",
            "dir":"asc"
            },
            {
            "field":"updated_at",
            "dir":"asc"
            }
        ],
        "group":[]
    }

    response = requests.post(BASE_URL + f"{tenant_id}/api-grid", headers=TOKEN, json=payload)
   # print(BASE_URL + f"{tenant_id}/api-grid")
    assert response.status_code == 200

    data = response.json()
    # print(data["data"])
    assert len(data["data"]) >= 0

def test_create_api():
    random_number = get_unique_int_number()
    payload = {
        "Name": f"Pytest Create API - {random_number}",
        "Description":"API Created for Pytest",
        "Version":"1.1",
        "Status":"pending",
        "Environment":"development",
        "LogLevel":"debug",
        "Tags":[""],
        "Scope":"createapi"
    }

    response = requests.post(BASE_URL + f"{tenant_id}/api", headers=TOKEN, json=payload)
   # print(BASE_URL + f"{tenant_id}/api-grid")
    assert response.status_code == 200

    data = response.json()
    api_id = data["ID"]
    api_name = data["Name"]

    test_get_api_resp = get_api_by_id(api_id)
    assert test_get_api_resp.status_code == 200

    test_get_api_data = test_get_api_resp.json()
    test_get_api_name = test_get_api_data["Name"]
    assert test_get_api_name == api_name
