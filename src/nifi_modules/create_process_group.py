import requests
import urllib3
import os
from dotenv import load_dotenv

load_dotenv()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def create_process_group(nifi_client):
    processGroupCanvasID = os.getenv("PROCESS_GROUP_CANVAS_ID")
    x, y = 200.0, 300.0
    name = os.getenv("PROCESS_GROUP_NAME")

    url = f"{nifi_client.base_url}/process-groups/{processGroupCanvasID}/process-groups"
    headers = {
        "Authorization": f"Bearer {nifi_client.token}",
        "Content-Type": "application/json"
    }
    data = {
        "revision": {"version": 0},
        "component": {
            "name": name,
            "position": {"x": x, "y": y}
        }
    }

    response = requests.post(url, headers=headers, json=data, verify=False)

    if response.status_code == 201:
        pg = response.json()
        print("Process Group created successfully")
        print("Process Group ID:", pg["id"])
    else:
        print("Failed to create Process Group:", response.status_code)
        print(response.text)
