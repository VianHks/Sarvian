import requests
import json
from helper import api_redis_id,create_endpoint, get_endpoint_by_id, get_token, get_tenant_id, get_api_id, get_base_url, get_data_source, get_unique_int_number, create_api_by_data_source, get_api_by_data_source_id


BASE_URL = get_base_url()
tenant_id = get_tenant_id()
TOKEN = get_token()
api_id = get_api_id()
data_source = get_data_source("redis")

def test_get_redis_data_source():
    payload = {
        "take":10,
        "skip":0,
        "page":1,
        "pageSize":10,
        "group":[]
    }
    response = requests.post(BASE_URL + f"{tenant_id}/{api_redis_id}/filter-grid/{data_source}", headers=TOKEN, json=payload)
    assert response.status_code == 200
    
    data = response.json()
    # print(data)
    assert len(data["data"]) >= 0

    
    