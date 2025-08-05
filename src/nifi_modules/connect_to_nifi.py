import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class NiFiClient:
    def __init__(self, base_url, username, password):
        self.base_url = base_url.rstrip('/')
        self.username = username
        self.password = password
        self.token = None

    def connect_and_print_about(self):
        if self.get_token():
            about = self.get_about()
            if about:
                print("Connected to NiFi!")
                print(about)
            else:
                print("Failed to retrieve NiFi info.")
        else:
            print("Authentication failed.")

    def get_token(self):
        url = f"{self.base_url}/access/token"
        data = {"username": self.username, "password": self.password}
        response = requests.post(url, data=data, verify=False)
        if response.status_code in (200, 201):
            self.token = response.text.strip()
            return True
        else:
            print("Failed to get token:", response.status_code, response.text)
            return False

    def get_about(self):
        if not self.token:
            print("No token found. Call get_token() first.")
            return None
        url = f"{self.base_url}/flow/about"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(url, headers=headers, verify=False)
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to get NiFi info:", response.status_code, response.text)
            return None
