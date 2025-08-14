import requests
from typing import Dict, Any, List
from src.utils import creation_succeeded
def create_parameter_context(nifi_client, name: str, description: str, parameters: List[Dict[str, Any]]) -> Dict[str, Any]:

    url = f"{nifi_client.base_url}/parameter-contexts"
    headers = {
        "Authorization": f"Bearer {nifi_client.token}",
        "Content-Type": "application/json"
    }

    data = {
        "revision": {"version": 0},
        "component": {
            "name": name,
            "description": description,
            "parameters": [
                {
                    "parameter": {
                        "name": param["name"],
                        "value": param.get("value"),
                        "sensitive": param.get("sensitive", False)
                    }
                } for param in parameters
            ]
        }
    }

    response = requests.post(url, headers=headers, json=data, verify=False)

    if creation_succeeded(response):
        context = response.json()
        print("Parameter Context created successfully")
        print("Parameter Context ID:", context["id"])
        return context
    else:
        print("Failed to create Parameter Context:", response.status_code)
        print(response.text)
        return {"error": response.text}
