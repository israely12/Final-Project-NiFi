import requests
from typing import Dict, Any
from configuration import PROCESS_GROUP_ID
def update_process_group_name(nifi_client, new_name) -> Dict[str, Any]:
    processGroupID = PROCESS_GROUP_ID

    get_url = f"{nifi_client.base_url}/process-groups/{processGroupID}"
    headers = {
        "Authorization": f"Bearer {nifi_client.token}",
        "Content-Type": "application/json"
    }

    get_response = requests.get(get_url, headers=headers, verify=False)
    if get_response.status_code != 200:
        print("Failed to fetch Process Group:", get_response.status_code)
        print(get_response.text)
        return {"error": get_response.text}

    process_group_data = get_response.json()

    process_group_data["component"]["name"] = new_name

    put_url = f"{nifi_client.base_url}/process-groups/{processGroupID}"
    put_response = requests.put(put_url, headers=headers, json=process_group_data, verify=False)

    if put_response.status_code == 200:
        updated_pg = put_response.json()
        print("Process Group name updated successfully")
        return updated_pg
    else:
        print("Failed to update Process Group name:", put_response.status_code)
        print(put_response.text)
        return {"error": put_response.text}
