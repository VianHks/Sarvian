import requests
import json
from helper import create_api_by_data_source, get_data_source, create_endpoint, get_tenant_id, get_token, get_api_id, get_unique_int_number, get_api_by_data_source_id, get_base_url

BASE_URL = get_base_url()
CUSTOM_FUNCTION_URL = get_base_url("custom_function")
api_id = get_api_id()
data_source = get_data_source("nextbytes_send_email")
nextbytes_doc_generator_data_source = get_data_source("nextbytes,doc")
TOKEN = get_token()
tenant_id = get_tenant_id()
doc_generator_data_source = get_data_source("nextbytes_doc_generator")

def test_get_nextbytes_api_list_by_data_source():
    payload = {
        "take":10,
        "skip":0,
        "page":1,
        "pageSize":10,
        "group":[]
    }
    response = requests.post(BASE_URL + f"{tenant_id}/{api_id}/filter-grid/{nextbytes_doc_generator_data_source}", headers=TOKEN, json=payload)
   # print(BASE_URL + f"{tenant_id}/api-grid")
    assert response.status_code == 200

    data = response.json()
    # print(data)
    assert data["total"] >= 0

def test_get_nextbytes_send_email_list():
    payload = {
        "url":"https://nextmail-api.cloud.nextplatform.ai/api/transactionals/",
        "type":"mail",
        "apiKey":"1a97a681-1563-4d18-b965-110ff95c8564:YZonYRiBrDnNgcijzeb58Cp6vcuUOKlU"
    }
    response = requests.post(BASE_URL + f"{tenant_id}/{api_id}/nextbytes", headers=TOKEN, json=payload)
   # print(BASE_URL + f"{tenant_id}/api-grid")
    assert response.status_code == 200

    data = response.json()
    # print(data)
    assert len(data["body"]["data"]["results"]) >= 0

def test_get_nextbytes_generate_document_list():
    payload = {
        "url":"https://nextmail-api.cloud.nextplatform.ai/api",
        "type":"document",
        "docType":"pdf",
        "apiKey":"1a97a681-1563-4d18-b965-110ff95c8564:YZonYRiBrDnNgcijzeb58Cp6vcuUOKlU"
    }
    response = requests.post(BASE_URL + f"{tenant_id}/{api_id}/nextbytes", headers=TOKEN, json=payload)
   # print(BASE_URL + f"{tenant_id}/api-grid")
    assert response.status_code == 200

    data = response.json()
    # print(data)
    assert len(data["body"]["data"]["results"]) >= 0

def test_create_nextbytes_send_email_api_by_data_source():
    number = get_unique_int_number()
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
    response = requests.post(BASE_URL + f"{tenant_id}/{api_id}/filter/{data_source}", headers=TOKEN, json=payload)
    assert response.status_code == 200

    data = response.json()
    # print(data)
    # API_ID_data = data["APIID"]
    assert data["APIID"] == int(api_id)
    assert data["Name"] == f"Pytest Send Email - {number}"

def test_edit_nextbytes_send_email_api_by_data_source():
    create_api = create_api_by_data_source("nextbytes_send_email")
    assert create_api.status_code == 200
    
    create_api_data = create_api.json()
    create_api_name = create_api_data["Name"]
    create_api_id = create_api_data["ID"]

    payload = {
        "Name": create_api_name,
        "Type": "next_bytes",
        "Description": "Send Email Created and Edited by Pytest",
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
            "attribs_detail": [],
            "ID": create_api_id
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
    assert test_get_api_desc == "Send Email Created and Edited by Pytest"

def test_delete_nextbytes_send_email_api_by_data_source_id():
    create_api = create_api_by_data_source("nextbytes_send_email")
    assert create_api.status_code == 200
    
    create_api_data = create_api.json()
    create_api_id = create_api_data["ID"]

    response = requests.delete(BASE_URL + f"{tenant_id}/{api_id}/filter/{create_api_id}", headers=TOKEN)
    assert response.status_code == 200

    test_get_api = get_api_by_data_source_id(create_api_id)
    test_get_api_data = test_get_api.json()
    assert test_get_api.status_code == 400
    assert test_get_api_data["detail"] == f"query Filter Definition ID {create_api_id} failed: record not found"

def test_update_nextbytes_send_email_endpoint():
    create_api = create_api_by_data_source("nextbytes_send_email")
    assert create_api.status_code == 200
    
    create_api_data = create_api.json()
    create_api_name = create_api_data["Name"]
    create_api_id = create_api_data["ID"]
    create_api_global_id = create_api_data["GlobalID"]

    test_create_endpoint = create_endpoint("nextbytes_send_email")
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
            "Type": "next_bytes",
            "Summary": "Send Email Created and Edited by Pytest",
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
                "attribs_detail": [],
                "ID": int(create_api_id),
                "id": create_api_global_id
            },
            "EndpointID": int(test_create_endpoint_id)
            }
        ]
    }
    update_pipeline = requests.put(BASE_URL + f"{tenant_id}/{test_create_endpoint_id}/pipelines/", headers=TOKEN, json=update_pipeline_payload)
    assert update_pipeline.status_code == 200

    edit_nextbytes_payload = {
        "Name": create_api_name,
        "Type": "next_bytes",
        "Description": "Send Email Created and Edited by Pytest",
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
            "attribs_detail": [],
            "ID": create_api_id
        }
    }
    update_nextbytes = requests.put(BASE_URL + f"{tenant_id}/{api_id}/filter/{data_source}/{create_api_id}", headers=TOKEN, json=edit_nextbytes_payload)
    assert update_nextbytes.status_code == 200

    update_endpoint_nextbytes_payload = {
        "Endp": [
            int(test_create_endpoint_id)
        ],
        "Spec": {
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
            "attribs_detail": [],
            "ID": create_api_id,
            "id": create_api_global_id
        }
    }
    update_nextbytes = requests.post(BASE_URL + f"{tenant_id}/{api_id}/filter/updatefilter/{data_source}/{create_api_id}", headers=TOKEN, json=update_endpoint_nextbytes_payload)
    update_nextbytes_data = update_nextbytes.json()
    # print(update_nextbytes_data)
    assert update_nextbytes.status_code == 200
    assert update_nextbytes_data["status"] == "succes"

def test_create_nextbytes_generate_document_api_by_data_source():
    number = get_unique_int_number()
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
    response = requests.post(BASE_URL + f"{tenant_id}/{api_id}/filter/{doc_generator_data_source}", headers=TOKEN, json=payload)
    assert response.status_code == 200

    data = response.json()
    # print(data)
    # API_ID_data = data["APIID"]
    assert data["APIID"] == int(api_id)
    assert data["Name"] == f"Pytest Generate Document - {number}"

def test_edit_nextbytes_generate_document_api_by_data_source():
    create_api = create_api_by_data_source("nextbytes_doc_generator")
    assert create_api.status_code == 200
    
    create_api_data = create_api.json()
    create_api_name = create_api_data["Name"]
    create_api_id = create_api_data["ID"]

    payload = {
        "Name": create_api_name,
        "Type": "document_generator",
        "Description": "Generate Document Created and Edited by Pytest",
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
            ],
            "ID": create_api_id
        }
    }
    response = requests.put(BASE_URL + f"{tenant_id}/{api_id}/filter/{doc_generator_data_source}/{create_api_id}", headers=TOKEN, json=payload)
    # update_data = response.json()
    # print(update_data)
    assert response.status_code == 200

    test_get_api = get_api_by_data_source_id(create_api_id)
    assert test_get_api.status_code == 200
    test_get_api_data = test_get_api.json()
    test_get_api_desc = test_get_api_data["Description"]
    assert test_get_api_desc == "Generate Document Created and Edited by Pytest"

def test_delete_nextbytes_generate_document_api_by_data_source_id():
    create_api = create_api_by_data_source("nextbytes_doc_generator")
    assert create_api.status_code == 200
    
    create_api_data = create_api.json()
    create_api_id = create_api_data["ID"]

    response = requests.delete(BASE_URL + f"{tenant_id}/{api_id}/filter/{create_api_id}", headers=TOKEN)
    assert response.status_code == 200

    test_get_api = get_api_by_data_source_id(create_api_id)
    test_get_api_data = test_get_api.json()
    assert test_get_api.status_code == 400
    assert test_get_api_data["detail"] == f"query Filter Definition ID {create_api_id} failed: record not found"

def test_update_nextbytes_generate_document_endpoint():
    create_api = create_api_by_data_source("nextbytes_doc_generator")
    assert create_api.status_code == 200
    
    create_api_data = create_api.json()
    create_api_name = create_api_data["Name"]
    create_api_id = create_api_data["ID"]
    create_api_global_id = create_api_data["GlobalID"]

    test_create_endpoint = create_endpoint("nextbytes_doc_generator")
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
            "Type": "document_generator",
            "Summary": "Generate Document Created by Pytest",
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
                ],
                "ID": create_api_id,
                "id": create_api_global_id
            },
            "EndpointID": int(test_create_endpoint_id)
            }
        ]
    }
    update_pipeline = requests.put(BASE_URL + f"{tenant_id}/{test_create_endpoint_id}/pipelines/", headers=TOKEN, json=update_pipeline_payload)
    assert update_pipeline.status_code == 200

    edit_nextbytes_payload = {
        "Name": create_api_name,
        "Type": "document_generator",
        "Description": "Generate Document Created and Edited by Pytest",
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
            ],
            "ID": create_api_id
        }
    }
    update_nextbytes = requests.put(BASE_URL + f"{tenant_id}/{api_id}/filter/{nextbytes_doc_generator_data_source}/{create_api_id}", headers=TOKEN, json=edit_nextbytes_payload)
    assert update_nextbytes.status_code == 200

    update_endpoint_nextbytes_payload = {
        "Endp": [
            int(test_create_endpoint_id)
        ],
        "Spec": {
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
            ],
            "ID": create_api_id,
            "id": create_api_global_id
        }
    }
    update_nextbytes = requests.post(BASE_URL + f"{tenant_id}/{api_id}/filter/updatefilter/{nextbytes_doc_generator_data_source}/{create_api_id}", headers=TOKEN, json=update_endpoint_nextbytes_payload)
    update_nextbytes_data = update_nextbytes.json()
    # print(update_nextbytes_data)
    assert update_nextbytes.status_code == 200
    assert update_nextbytes_data["status"] == "succes"

