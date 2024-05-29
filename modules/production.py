import requests
from urllib.parse import urljoin
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


class Production:
    def __init__(self, token):
        self.token = token

    def get_daily_production(self, start_date, end_date):
        url = urljoin(BASEURL, f"site/{SITE_ID}/energy")
        params = {
            'api_key': SITE_TOKEN,
            'timeUnit': 'DAY',
            'startDate': start_date.strftime('%Y-%m-%d'),
            'endDate': end_date.strftime('%Y-%m-%d')
        }

        print("Request URL:", url)
        print("Request Params:", params)
        r = requests.get(url, params=params)
        print("Response:", r.content)
        r.raise_for_status()
        return r.json()

    def print_daily_production(self, daily_production):
        output = "Daily Production:\n"
        unit = daily_production['energy'].get('unit')
        for day in daily_production['energy']['values']:
            output += (
                f"Date: {day['date']}, \nProduction: {day['value']} {unit}\n"
            )
        return output
