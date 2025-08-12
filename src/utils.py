import requests
from typing import Tuple, Dict, Any, Optional

def creation_succeeded(response: requests.Response) -> bool:
    return response.status_code in (200, 201)

def set_coordinates(x: Optional[float] = None, y: Optional[float] = None) -> Tuple[float, float]:
    default_x, default_y = 400.0, 100.0
    return (x if x is not None else default_x, y if y is not None else default_y)

def build_request(
    nifi_client: Any,
    process_group_id: str,
    component_type: str,
    component_payload: Dict[str, Any],
    x: Optional[float] = None,
    y: Optional[float] = None
) -> Tuple[str, Dict[str, str], Dict[str, Any]]:

    x, y = set_coordinates(x, y)

    url = f"{nifi_client.base_url}/process-groups/{process_group_id}/{component_type}"
    headers = {
        "Authorization": f"Bearer {nifi_client.token}",
        "Content-Type": "application/json"
    }
    data = {
        "revision": {"version": 0},
        "component": {
            **component_payload,
            "position": {"x": x, "y": y}
        }
    }
    return url, headers, data
