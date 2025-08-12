import requests
from typing import Dict, Any
from src.utils import creation_succeeded


def create_connection(nifi_client, parent_group_id: str, source_port_id: str, source_pg_id: str,
                      dest_port_id: str, dest_pg_id: str) -> Dict[str, Any]:
    url = f"{nifi_client.base_url}/process-groups/{parent_group_id}/connections"
    headers = {
        "Authorization": f"Bearer {nifi_client.token}",
        "Content-Type": "application/json"
    }

    data = {
        "revision": {"version": 0},
        "component": {
            "name": "PG1-to-PG2-Connection",
            "source": {
                "id": source_port_id,
                "type": "OUTPUT_PORT",
                "groupId": source_pg_id
            },
            "destination": {
                "id": dest_port_id,
                "type": "INPUT_PORT",
                "groupId": dest_pg_id
            },
            "parentGroupId": parent_group_id
        }
    }

    response = requests.post(url, headers=headers, json=data, verify=False)

    if creation_succeeded(response):
        connection = response.json()
        print("Connection created successfully")
        print("Connection ID:", connection["id"])
        return connection
    else:
        print("Failed to create connection:", response.status_code)
        print(response.text)
        return {"error": response.text}
