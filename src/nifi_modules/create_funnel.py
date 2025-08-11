import requests
import urllib3
import os
from dotenv import load_dotenv

load_dotenv()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def create_funnel(nifi_client):
    ProcessGroupCanvasID = os.getenv("PROCESS_GROUP_CANVAS_ID")
    x, y = 400.0, 100.0

    url = f"{nifi_client.base_url}/process-groups/{ProcessGroupCanvasID}/funnels"
    headers = {
        "Authorization": f"Bearer {nifi_client.token}",
        "Content-Type": "application/json"
    }
    data = {
        "revision": {"version": 0},
        "component": {"position": {"x": x, "y": y}}
    }

    response = requests.post(url, headers=headers, json=data, verify=False)

    if response.status_code == 201:
        funnel = response.json()
        print("Funnel created successfully")
        print("Funnel ID:", funnel["id"])
        return funnel
    else:
        print("Failed to create funnel:", response.status_code)
        print(response.text)
        return {"error": response.text}
