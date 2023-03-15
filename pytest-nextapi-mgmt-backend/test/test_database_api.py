import requests
import json
from helper import get_ddl_database, get_base_url, get_token, get_tenant_id, get_api_id, create_database_connection, get_database_connection, get_unique_int_number, get_database_by_id, get_connection_id, create_database

BASE_URL = get_base_url()
tenant_id = get_tenant_id()
TOKEN = get_token()
api_id = get_api_id()
connection_id = get_connection_id()
database_type = "table"
database_name = "public.demo_uuid"
database_id = "1815"

def test_get_database_datasource_list():
    payload = {
        "take":10,
        "skip":0,
        "page":1,
        "pageSize":10,
        "group":[]
    }
    response =  requests.post(BASE_URL + f"{tenant_id}/{api_id}/database/datasource-grid", headers=TOKEN, json=payload)
    # data = response.json()
    # print(data)
    assert response.status_code == 200

    data = response.json()
    # print(data)
    assert data["total"] >= 0

def test_get_database_connection_list():
    payload = {
        "take":10,
        "skip":0,
        "page":1,
        "pageSize":10,
        "group":[]
    }
    response =  requests.post(BASE_URL + f"{tenant_id}/{api_id}/database/connection-grid", headers=TOKEN, json=payload)
    # data = response.json()
    # print(data)
    assert response.status_code == 200

    data = response.json()
    # print(data)
    assert data["total"] >= 0

def test_get_database_connection_db():
    params = {"env": 20}
    payload = {
        "DBType":"postgres",
        "Host":"10.10.16.201",
        "Login":"postgres",
        "Description":"db connection for pytest",
        "AdvancedSetting":[],
        "Name":"nextapi-test",
        "Port":4041,
        "Password":"{{SECRET:NEXTAPI_DEV_DB_PASSWORD}}",
        "CustomDatabase":[],
        "LowerCaseColumns":[]
    }
    response =  requests.post(BASE_URL + f"{tenant_id}/{api_id}/database/connection/db", headers=TOKEN, params=params, json=payload)
    assert response.status_code == 200

    data = response.json()
    # print(data)
    assert len(data) >= 0

def test_create_database_connection():
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
    response = requests.post(BASE_URL + f"{tenant_id}/{api_id}/database/connection/", headers=TOKEN, json=payload)
    assert response.status_code == 200

    data = response.json()
    data_name = data["Name"]
    assert data_name == "nextapi-test"

def test_get_database_connection_by_id():
    response = requests.get(BASE_URL + f"{tenant_id}/{api_id}/database/connection/{connection_id}", headers=TOKEN)
    assert response.status_code == 200

    data = response.json()
    # print(data)
    assert data["Name"] == "nextapi-test"

def test_delete_database_connection():
    test_create_database_connection = create_database_connection()
    assert test_create_database_connection.status_code == 200
    test_create_database_connection_data = test_create_database_connection.json()
    test_create_database_connection_id = test_create_database_connection_data["ID"]

    response = requests.delete(BASE_URL + f"{tenant_id}/{api_id}/database/connection/{test_create_database_connection_id}", headers=TOKEN)
    assert response.status_code == 200

    test_get_database_connection = get_database_connection(test_create_database_connection_id)
    test_get_database_connection_data = test_get_database_connection.json()
    # print(test_get_business_logic_data)
    assert test_get_database_connection.status_code == 400
    assert test_get_database_connection_data["detail"] == "query database connection failed: record not found"

def test_update_database_connection():
    test_create_database_connection = create_database_connection()
    assert test_create_database_connection.status_code == 200
    test_create_database_connection_data = test_create_database_connection.json()
    test_create_database_connection_id = test_create_database_connection_data["ID"]

    payload = {
        "DBType":"postgres",
        "Host":"10.10.16.201",
        "Login":"postgres",
        "Description":"db connection for pytest",
        "ThreadsCount":1,
        "Name":"nextapi-test",
        "Port":4041,
        "Password":"{{SECRET:NEXTAPI_DEV_DB_PASSWORD}}",
        "DBName":"postgres",
        "LowerCaseColumns":[],
        "UseUpperCaseColumnNames":True
    }
    response = requests.put(BASE_URL + f"{tenant_id}/{api_id}/database/connection/{test_create_database_connection_id}", headers=TOKEN, json=payload)
    assert response.status_code == 200

    test_get_database_connection = get_database_connection(test_create_database_connection_id)
    test_get_database_connection_data = test_get_database_connection.json()
    # print(test_get_business_logic_data)
    assert test_get_database_connection.status_code == 200
    assert test_get_database_connection_data["DBName"] == "postgres"

def test_get_database_connection():
    params = {"type": "postgres"}
    response = requests.get(BASE_URL + f"{tenant_id}/{api_id}/database/connection", headers=TOKEN, params=params)
    assert response.status_code == 200

    data = response.json()
    # print(data)
    assert len(data) >= 0

def test_get_database_type():
    params = {"env": 20}
    response = requests.get(BASE_URL + f"{tenant_id}/{api_id}/database/list-object/{connection_id}/{database_type}", headers=TOKEN, params=params)
    assert response.status_code == 200

    data = response.json()
    # print(data)
    assert len(data) >= 0

def test_get_column_from_database():
    params = {"env": 20}
    response = requests.get(BASE_URL + f"{tenant_id}/{api_id}/database/list-column/{connection_id}/{database_type}/{database_name}", headers=TOKEN, params=params)
    assert response.status_code == 200

    data = response.json()
    # print(data)
    assert len(data) >= 0

def test_get_database_by_id():
    response = requests.get(BASE_URL + f"{tenant_id}/{api_id}/database/datasource/{database_id}", headers=TOKEN)
    assert response.status_code == 200

    data = response.json()
    # print(data)
    assert data["Name"] == "Test Database by Pytest"

def test_create_database():
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
    response = requests.post(BASE_URL + f"{tenant_id}/{api_id}/database/datasource/{connection_id}", headers=TOKEN, params=params, json=payload)
    # test_data = response.json()
    # print(BASE_URL + f"{tenant_id}/{api_id}/database/datasource/{connection_id}")
    # print(test_data)
    assert response.status_code == 200

    data = response.json()
    create_database_id = data["ID"]

    test_get_database = get_database_by_id(create_database_id)
    assert test_get_database.status_code == 200
    test_get_database_data = test_get_database.json()
    assert test_get_database_data["Name"] == f"Create Database by Pytest - {random_number}"

def test_delete_database():
    test_create_database = create_database()
    assert test_create_database.status_code == 200
    test_create_database_data = test_create_database.json()
    test_create_database_id = test_create_database_data["ID"]

    response = requests.delete(BASE_URL + f"{tenant_id}/{api_id}/database/datasource/{test_create_database_id}", headers=TOKEN)
    assert response.status_code == 200

    test_get_database = get_database_by_id(test_create_database_id)
    test_get_database_data = test_get_database.json()
    # print(test_get_business_logic_data)
    assert test_get_database.status_code == 400
    assert test_get_database_data["detail"] == "query database filter failed: record not found"

def test_update_database():
    test_create_database = create_database()
    assert test_create_database.status_code == 200
    test_create_database_data = test_create_database.json()
    # print(test_create_database_data)
    test_create_database_id = test_create_database_data["ID"]
    test_create_database_GlobalID = test_create_database_data["GlobalID"]
    test_create_database_name = test_create_database_data["Name"]

    payload = {
        "Name": test_create_database_name,
        "SQLType":"table",
        "SQL":"public.demo_uuid",
        "ConnectionID":int(connection_id),
        "Operations":[{"Operation":"select"}],
        "GenerateEndpoints":False,
        "GlobalID":test_create_database_GlobalID,
        "Details":[
            {
                "Alias":"",
                "Name":"id",
                "DataType":"integer",
                "ItemType":"",
                "Length":32,
                "Nullable":False,
                "PrimaryKey":True,
                "Type":"column",
                "AutoIncrement":False,
                "Mapping":{
                    "input":{
                        "grpc_message":["sad"],
                        "array_marker":["sad"]
                    },
                    "output":{
                        "generic_context":"sad",
                        "array_marker":["sad"]
                    }
                },
                "No":1
            }
        ]
    }
    response = requests.put(BASE_URL + f"{tenant_id}/{api_id}/database/datasource/{connection_id}/{test_create_database_id}", headers=TOKEN, json=payload)
    # response_data = response.json()
    # print(response_data)
    assert response.status_code == 200

    test_get_database = get_database_by_id(test_create_database_id)
    test_get_database_data = test_get_database.json()
    # print(test_get_database_data["Details"][0]["Mapping"]["output"]["generic_context"])
    assert test_get_database.status_code == 200
    assert test_get_database_data["Details"][0]["Mapping"]["output"] == {'array_marker': ['sad'], 'generic_context': 'sad'}

def test_get_ddl_database():
    params = {"env": 20}
    response = requests.get(BASE_URL + f"{tenant_id}/{api_id}/database/ddl-table/{connection_id}/{database_name}", headers=TOKEN, params=params)
    # print(BASE_URL + f"{tenant_id}/{api_id}/database/ddl-table/{connection_id}/{database_name}")
    # print(data)
    assert response.status_code == 200

    data = response.json()
    # print(data)
    assert len(data["Columns"]) >= 0

def test_get_database_data_type():
    response = requests.get(BASE_URL + f"{tenant_id}/{api_id}/database/data-type/{connection_id}", headers=TOKEN)
    # print(BASE_URL + f"{tenant_id}/{api_id}/database/ddl-table/{connection_id}/{database_name}")
    # print(data)
    assert response.status_code == 200

    data = response.json()
    # print(data)
    assert len(data) > 0

def test_query_database():
    query = "SELECT * FROM public.demo_uuid"
    params = {"env": 20}
    response =  requests.post(BASE_URL + f"{tenant_id}/{api_id}/database/query/{connection_id}", headers=TOKEN, params=params, data=query)
    data = response.json()
    # print(data)
    assert response.status_code == 200

    data = response.json()
    # print(data)
    assert len(data["Columns"]) >= 0

def test_get_cluster():
    payload = {
        "take":100,
        "skip":0,
        "page":1,
        "pageSize":100,
        "filter":{
            "logic":"and",
            "filters":[
                {
                    "field":"environment_id",
                    "operator":"eq",
                    "value":"20"
                }
            ]
        },
        "group":[]
    }
    response =  requests.post(BASE_URL + f"{tenant_id}/env/variable-grid", headers=TOKEN, json=payload)
    data = response.json()
    # print(data)
    assert response.status_code == 200

    data = response.json()
    # print(data)
    assert len(data) >= 0

def test_update_ddl_table():
    number = get_unique_int_number()
    params = {"env": 20}
    payload = {
        "Name":"public.demo_uuid",
        "RenameColumns":[],
        "UpdateColumns":[],
        "AddColumns":[
            {
                "Name": f"pytest_column_{number}",
                "DataType":"boolean",
                "Nullable":"YES",
                "PrimaryKey":False
            }
        ],
        "RemoveColumns":[],
        "AddForeignKeys":[],
        "RemoveForeignKeys":[],
        "AddCheckConstraints":[],
        "RemoveCheckConstraints":[],
        "AddUniqueConstraints":[],
        "RemoveUniqueConstraints":[]
    }
    response = requests.put(BASE_URL + f"{tenant_id}/{api_id}/database/ddl-table/{connection_id}", headers=TOKEN, params=params, json=payload)
    assert response.status_code == 200

    get_ddl = get_ddl_database(connection_id)
    assert get_ddl.status_code == 200
    get_ddl_data = get_ddl.json()
    column_length = len(get_ddl_data["Columns"]) - 1
    assert get_ddl_data["Columns"][column_length]["Name"] == f"pytest_column_{number}"




