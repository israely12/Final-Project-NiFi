import requests
from typing import Dict, Any
from configuration import PROCESS_GROUP_ID
from src.utils import build_request, creation_succeeded
def create_output_port(nifi_client) -> Dict[str, Any]:
    component_payload = {
        "name": "Ulik OutputPort"
    }

    url, headers, data = build_request(nifi_client, PROCESS_GROUP_ID, "output-ports", component_payload)

    response = requests.post(url, headers=headers, json=data, verify=False)

    if creation_succeeded(response):
        port = response.json()
        print("OutputPort created successfully")
        print("OutputPort ID:", port["id"])
        return port
    else:
        print("Failed to create OutputPort:", response.status_code)
        print(response.text)
        return {"error": response.text}
