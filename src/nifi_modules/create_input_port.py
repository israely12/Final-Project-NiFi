import requests
import os
from dotenv import load_dotenv

load_dotenv()
def create_input_port(nifi_client):
    process_group_id = os.getenv("PROCESS_GROUP_ID")
    x, y = 100.0, 200.0

    url = f"{nifi_client.base_url}/process-groups/{process_group_id}/input-ports"
    headers = {
        "Authorization": f"Bearer {nifi_client.token}",
        "Content-Type": "application/json"
    }
    data = {
        "revision": {"version": 0},
        "component": {
            "name": "Ulik InputPort",
            "position": {"x": x, "y": y}
        }
    }

    response = requests.post(url, headers=headers, json=data, verify=False)

    if response.status_code == 201:
        port = response.json()
        print("InputPort created successfully")
        print("InputPort ID:", port["id"])
        return port
    else:
        print("Failed to create InputPort:", response.status_code)
        print(response.text)
        return {"error": response.text}
