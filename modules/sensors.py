import requests
import logging
import os

logging.basicConfig(level=logging.DEBUG)
logging.getLogger("main").setLevel(logging.DEBUG)

# Load environment variables
SITE_TOKEN = os.getenv("SITE_TOKEN")
SITE_ID = os.getenv("SITE_ID")
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

BASE_URL = "https://monitoringapi.solaredge.com/"


class Sensors:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_sensor_data(self, SITE_ID):
        url = (
            f"{BASE_URL}{SITE_ID}/sensors"
        )
        params = {'api_key': self.api_key}
        response = requests.get(url, params=params)
        print("DEBUG: Request URL:", response.url)
        if response.status_code == 200:
            return response.json()
        else:
            print("DEBUG: Response Status Code:", response.status_code)
            print("DEBUG: Response Content:", response.text)
            return None

    def format_sensor_data(self, sensor_data):
        if 'total' in sensor_data and sensor_data['total'] > 0:
            sensor_list = sensor_data['list']
            formatted_data = "Sensor Data:\n"
            for sensor in sensor_list:
                # Format each sensor data here
                formatted_data += f"Sensor ID: {sensor['id']}\n"
                # Add more details about the sensor as needed
            return formatted_data
        else:
            return "No sensors available for this site"
