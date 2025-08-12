from typing import Dict, Any
from src.nifi_modules.create_input_port import create_input_port
from src.nifi_modules.create_output_port import create_output_port
from src.nifi_modules.create_process_group import create_process_group

def create_full_process_group_setup(nifi_client) -> Dict[str, Any]:
    process_group = create_process_group(nifi_client)
    if "error" in process_group:
        return process_group

    process_group_id = process_group.get("id")
    if not process_group_id:
        return {"error": "Process Group ID not found in response"}

    input_port = create_input_port(nifi_client, process_group_id)
    if "error" in input_port:
        return input_port

    output_port = create_output_port(nifi_client, process_group_id)
    if "error" in output_port:
        return output_port

    return {
        "process_group": process_group,
        "input_port": input_port,
        "output_port": output_port
    }
