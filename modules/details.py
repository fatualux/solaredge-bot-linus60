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

BASEURL = "https://monitoringapi.solaredge.com/site/"


class Details:
    def __init__(self, token):
        self.token = token

    def get_details(self, SITE_ID):
        base_url = urljoin(BASEURL, f"{SITE_ID}/details")
        url = f"{base_url}?api_key={self.token}"
        print("Request URL:", url)
        response = requests.get(url)
        response.raise_for_status()
        try:
            site_details = response.json()
        except ValueError:
            raise ValueError("Failed to parse response as JSON")
        return site_details

    def format_site_details(self, details):
        details = details['details']
        formatted_details = "Site Details:\n"
        formatted_details += (
            f"id: {details['id']}\n"
            f"name: {details['name']}\n"
            f"accountId: {details['accountId']}\n"
            f"status: {details['status']}\n"
            f"peakPower: {details['peakPower']}\n"
            f"lastUpdateTime: {details['lastUpdateTime']}\n"
            f"installationDate: {details['installationDate']}\n"
            f"ptoDate: {details['ptoDate']}\n\n"
            f"Location:\n"
            f"country: {details['location']['country']}\n"
            f"city: {details['location']['city']}\n"
            f"address: {details['location']['address']}\n\n"
            f"PrimaryModule:\n"
            f"manufacturerName: {details['primaryModule']['manufacturerName']}\n"
            f"modelName: {details['primaryModule']['modelName']}\n"
            f"maximumPower: {details['primaryModule']['maximumPower']}\n"
            f"temperatureCoef: {details['primaryModule']['temperatureCoef']}\n"
            f"{urljoin(BASEURL, '/site/' + str(details['id']))}\n"
            f"\n"
        )
        return formatted_details
