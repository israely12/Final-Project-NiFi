from src.nifi_modules.connect_to_nifi import NiFiClient
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    client = NiFiClient(
        base_url=os.getenv("NIFI_BASE_URL"),
        username=os.getenv("MY_NIFI_USERNAME"),
        password=os.getenv("MY_NIFI_PASSWORD")
    )
    client.connect_and_print_about()

if __name__ == "__main__":
    main()
