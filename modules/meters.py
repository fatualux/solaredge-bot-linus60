import requests
from urllib.parse import urljoin
from datetime import datetime
import logging
import os

logging.basicConfig(level=logging.DEBUG)
logging.getLogger("main").setLevel(logging.DEBUG)

# Load environment variables
SITE_TOKEN = os.getenv("SITE_TOKEN")
SITE_ID = os.getenv("SITE_ID")
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

BASEURL = "https://monitoringapi.solaredge.com/"


class Meters:
    def __init__(self, SITE_TOKEN, SITE_ID, meters=None, time_unit='DAY'):
        self.SITE_TOKEN = SITE_TOKEN
        self.SITE_ID = SITE_ID
        self.meters = meters
        self.time_unit = time_unit

    def get_meter_data(self):
        end_time = datetime.now()
        # Set start time to 7:00 AM
        start_time = datetime(
            end_time.year, end_time.month, end_time.day, 7, 0, 0
        )

        url = urljoin(BASEURL, f"site/{self.SITE_ID}/meters")
        params = {
            'api_key': self.SITE_TOKEN,
            'startTime': start_time.strftime('%Y-%m-%d %H:%M:%S'),
            'endTime': end_time.strftime('%Y-%m-%d %H:%M:%S'),
            'timeUnit': self.time_unit
        }

        if self.meters:
            params['meters'] = self.meters

        print("Request URL:", url)
        print("Request Params:", params)
        r = requests.get(url, params=params)
        print("Response:", r.content)
        r.raise_for_status()
        return r.json()

    def print_meter_data(self, meter_data):
        meter_info = ""
        meter_info += "Meter Data:\n"
        meter_energy_details = meter_data.get('meterEnergyDetails')
        if meter_energy_details:
            meters = meter_energy_details.get('meters')
            if meters:
                unique_meters = {}
                for meter in meters:
                    meter_serial_number = meter.get('meterSerialNumber')
                    meter_type = meter.get('meterType')
                    key = (meter_serial_number, meter_type)
                    if key not in unique_meters:
                        unique_meters[key] = True
                        meter_info += (
                            f"Meter Serial Number: {meter_serial_number}\n"
                            f"Connected SolarEdge Device SN: "
                            f"{meter.get('connectedSolaredgeDeviceSN')}\n"
                            f"Meter Type: {meter_type}\n"
                            "Values:\n"
                        )
                        for value in meter.get('values'):
                            meter_info += (
                                f"  Date: {value.get('date')}, "
                                f"Value: {value.get('value')} "
                                f"{meter_energy_details.get('unit')}\n"
                            )
                        meter_info += "\n"
        else:
            meter_info += "No meter data found."

        return meter_info
