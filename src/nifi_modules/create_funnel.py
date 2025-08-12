import requests
from configuration import PROCESS_GROUP_CANVAS_ID
from dotenv import load_dotenv
from src.utils import creation_succeeded, build_request
from typing import Dict, Any
from src.nifi_modules.connect_to_nifi import NiFiClient

load_dotenv()
def create_funnel(nifi_client:NiFiClient) -> Dict[str, Any]:
    url, headers, data = build_request(nifi_client, PROCESS_GROUP_CANVAS_ID, "funnels", {})
    response = requests.post(url, headers=headers, json=data, verify=False)

    if creation_succeeded(response):
        funnel = response.json()
        print("Funnel created successfully")
        print("Funnel ID:", funnel["id"])
        return funnel
    else:
        print("Failed to create funnel:", response.status_code)
        print(response.text)
        return {"error": response.text}
