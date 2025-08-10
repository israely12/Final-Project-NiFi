from src.nifi_modules.connect_to_nifi import NiFiClient
from src.nifi_modules.create_funnel import create_funnel
from src.nifi_modules.create_process_group import create_process_group
from src.nifi_modules.get_process_group_by_id import get_process_group_by_id
from src.nifi_modules.update_process_group_name import update_process_group_name
from src.rest_api.run_flask import create_app
import os
from dotenv import load_dotenv

load_dotenv()

MODE = os.getenv("RUN_MODE")

new_process_group_name = os.getenv("UPDATE_PROCESS_GROUP")
def run_modules():
    client = NiFiClient(
        base_url=os.getenv("NIFI_BASE_URL"),
        username=os.getenv("MY_NIFI_USERNAME"),
        password=os.getenv("MY_NIFI_PASSWORD")
    )
    client.connect_and_print_about()
    create_funnel(client)
    create_process_group(client)
    get_process_group_by_id(client)
    update_process_group_name(client,new_process_group_name)

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
