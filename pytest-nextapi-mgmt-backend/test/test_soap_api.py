import requests
import json
from helper import get_token, get_tenant_id, get_api_id, get_base_url, get_data_source, get_unique_int_number, create_api_by_data_source, get_api_by_data_source_id

BASE_URL = get_base_url()
tenant_id = get_tenant_id()
TOKEN = get_token()
api_id = get_api_id()
data_source = get_data_source("soap")

def test_get_soap_wsdl_info():
    response_data = "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"
    response =  requests.post(BASE_URL + f"{tenant_id}/{api_id}/soap/wsdlinfo", headers=TOKEN, data=response_data)
    # data = response.json()
    # print(data)
    assert response.status_code == 200

    data = response.json()
    # print(data)
    assert data["URL"] == response_data

def test_get_soap_api_by_data_source():
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

def test_create_soap_api_by_data_source():
    number = get_unique_int_number()
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
    response = requests.post(BASE_URL + f"{tenant_id}/{api_id}/filter/{data_source}", headers=TOKEN, json=payload)
    assert response.status_code == 200

    data = response.json()
    # print(data)
    # API_ID_data = data["APIID"]
    assert data["APIID"] == int(api_id)
    assert data["Name"] == f"Pytest SOAP - {number}"

def test_edit_soap_api_by_data_source():
    create_api = create_api_by_data_source("soap")
    assert create_api.status_code == 200
    
    create_api_data = create_api.json()
    create_api_name = create_api_data["Name"]
    create_api_id = create_api_data["ID"]

    payload = {
        "Name": f"{create_api_name}",
        "Type": "soap_data_source",
        "Description": "SOAP Created and Edited by Pytest",
        "Specification": {
            "PortType": "NumberConversionSoapType",
            "WsdlUrl": "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL",
            "Mode": "",
            "File": "",
            "WsdlPath": "",
            "WsdlMain": "wsdl.wsdl",
            "wsdl": "wsdl.wsdl",
            "operation": "NumberToWords",
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
        "Files": []
    }
    response = requests.put(BASE_URL + f"{tenant_id}/{api_id}/filter/{data_source}/{create_api_id}", headers=TOKEN, json=payload)
    # update_data = response.json()
    # print(update_data)
    assert response.status_code == 200

    test_get_api = get_api_by_data_source_id(create_api_id)
    assert test_get_api.status_code == 200
    test_get_api_data = test_get_api.json()
    test_get_api_desc = test_get_api_data["Description"]
    assert test_get_api_desc == "SOAP Created and Edited by Pytest"

def test_delete_soap_api_by_data_source_id():
    create_api = create_api_by_data_source("soap")
    assert create_api.status_code == 200
    
    create_api_data = create_api.json()
    create_api_id = create_api_data["ID"]

    response = requests.delete(BASE_URL + f"{tenant_id}/{api_id}/filter/{create_api_id}", headers=TOKEN)
    assert response.status_code == 200

    test_get_api = get_api_by_data_source_id(create_api_id)
    test_get_api_data = test_get_api.json()
    assert test_get_api.status_code == 400
    assert test_get_api_data["detail"] == f"query Filter Definition ID {create_api_id} failed: record not found"