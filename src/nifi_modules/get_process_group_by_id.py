import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_process_group_by_id(nifi_client):
    process_group_id = os.getenv("PROCESS_GROUP_ID")

    url = f"{nifi_client.base_url}/process-groups/{process_group_id}"
    headers = {
        "Authorization": f"Bearer {nifi_client.token}"
    }

    response = requests.get(url, headers=headers, verify=False)

    if response.status_code == 200:
        process_group = response.json()
        print("Process Group details fetched successfully")
        print(process_group)
    else:
        print("Failed to fetch Process Group:", response.status_code)
        print(response.text)
