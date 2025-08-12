from src.nifi_modules.connect_to_nifi import NiFiClient
from src.nifi_modules.create_funnel import create_funnel
from src.nifi_modules.create_process_group import create_process_group
from src.nifi_modules.get_process_group_by_id import get_process_group_by_id
from src.nifi_modules.update_process_group_name import update_process_group_name
from src.nifi_modules.create_input_port import create_input_port
from src.nifi_modules.create_output_port import create_output_port
from src.rest_api.run_flask import create_app
from configuration import NIFI_BASE_URL, MY_NIFI_USERNAME, MY_NIFI_PASSWORD, RUN_MODE, UPDATE_PROCESS_GROUP

MODE = RUN_MODE
new_process_group_name = UPDATE_PROCESS_GROUP
def run_modules():
    client = NiFiClient(
        base_url=NIFI_BASE_URL,
        username=MY_NIFI_USERNAME,
        password=MY_NIFI_PASSWORD
    )

    client.connect_and_print_about()
    # create_funnel(client)
    # create_process_group(client)
    # get_process_group_by_id(client)
    # update_process_group_name(client,new_process_group_name)
    # create_input_port(client)
    # create_output_port(client)

def run_api():
    app = create_app()
    app.run(debug=True)

if __name__ == "__main__":
    if MODE == "modules":
        run_modules()
    elif MODE == "api":
        run_api()
    else:
        print("error")
