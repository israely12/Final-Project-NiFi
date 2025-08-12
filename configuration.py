import os
from dotenv import load_dotenv

load_dotenv()

NIFI_BASE_URL = os.getenv("NIFI_BASE_URL", "https://localhost:8443/nifi-api")
MY_NIFI_USERNAME = os.getenv("MY_NIFI_USERNAME", "ae38de00-1c5b-40c8-a83a-c4a239555e67")
MY_NIFI_PASSWORD = os.getenv("MY_NIFI_PASSWORD", "Cnryve3KQIw0qgCP9hd9YlC/CrKRhLuh")
PROCESS_GROUP_CANVAS_ID = os.getenv("PROCESS_GROUP_CANVAS_ID", "75297329-0198-1000-c624-66468dc7321a")
PROCESS_GROUP_NAME = os.getenv("PROCESS_GROUP_NAME", "Ulik-Process-Group")
PROCESS_GROUP_ID = os.getenv("PROCESS_GROUP_ID", "844db5fe-0198-1000-ba0d-18db2ed15340")
RUN_MODE = os.getenv("RUN_MODE", "modules")
UPDATE_PROCESS_GROUP = os.getenv("UPDATE_PROCESS_GROUP", "ulik-update")
SOURCE_PORT_ID = os.getenv("SOURCE_PORT_ID", "9e6b1f45-0198-1000-a9a4-669c8831b453")
SOURCE_PG_ID = os.getenv("SOURCE_PG_ID", "844db5fe-0198-1000-ba0d-18db2ed15340")
DEST_PORT_ID = os.getenv("DEST_PORT_ID", "9e5b9b1c-0198-1000-1bfc-a108201aab4f")
DEST_PG_ID = os.getenv("DEST_PG_ID", "9db0602e-0198-1000-1856-e36f3b8b6c1c")
