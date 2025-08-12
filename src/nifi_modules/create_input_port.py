import requests
from typing import Dict, Any
from src.utils import build_request, creation_succeeded
from configuration import PROCESS_GROUP_ID

def create_input_port(nifi_client) -> Dict[str, Any]:
    component_payload = {
        "name": "Ulik InputPort"
    }

    url, headers, data = build_request(nifi_client, PROCESS_GROUP_ID, "input-ports", component_payload)

    response = requests.post(url, headers=headers, json=data, verify=False)

    if creation_succeeded(response):
        port = response.json()
        print("InputPort created successfully")
        print("InputPort ID:", port["id"])
        return port
    else:
        print("Failed to create InputPort:", response.status_code)
        print(response.text)
        return {"error": response.text}
