import requests
from typing import Dict, Any
from src.utils import build_request, creation_succeeded
from configuration import PROCESS_GROUP_CANVAS_ID, PROCESS_GROUP_NAME
def create_process_group(nifi_client) -> Dict[str, Any]:
    component_payload = {
        "name": PROCESS_GROUP_NAME
    }

    url, headers, data = build_request(nifi_client, PROCESS_GROUP_CANVAS_ID, "process-groups", component_payload)

    response = requests.post(url, headers=headers, json=data, verify=False)

    if creation_succeeded(response):
        processGroup = response.json()
        print("Process Group created successfully")
        print("Process Group ID:", processGroup["id"])
        return processGroup
    else:
        print("Failed to create Process Group:", response.status_code)
        print(response.text)
        return {"error": response.text}
