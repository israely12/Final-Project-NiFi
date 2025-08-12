import requests
from typing import Dict, Any
from configuration import PROCESS_GROUP_ID
from src.utils import creation_succeeded

def get_process_group_by_id(nifi_client) -> Dict[str, Any]:
    process_group_id = PROCESS_GROUP_ID

    url = f"{nifi_client.base_url}/process-groups/{process_group_id}"
    headers = {
        "Authorization": f"Bearer {nifi_client.token}"
    }

    response = requests.get(url, headers=headers, verify=False)

    if creation_succeeded(response):
        process_group = response.json()
        print("Process Group details fetched successfully")
        print(process_group)
        return process_group
    else:
        print("Failed to fetch Process Group:", response.status_code)
        print(response.text)
        return {"error": response.text}
