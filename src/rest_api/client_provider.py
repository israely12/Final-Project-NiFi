import os
from dotenv import load_dotenv
from src.nifi_modules.connect_to_nifi import NiFiClient

load_dotenv()

client = NiFiClient(
    base_url=os.getenv("NIFI_BASE_URL"),
    username=os.getenv("MY_NIFI_USERNAME"),
    password=os.getenv("MY_NIFI_PASSWORD")
)
client.connect_and_print_about()
