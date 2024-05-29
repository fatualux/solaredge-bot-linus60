import requests
from urllib.parse import urljoin
import re

base_url = "https://monitoringapi.solaredge.com/"


class Overview:
    def __init__(self, token):
        self.token = token

    def get_site_overview(self, site_id):
        """
        Get site overview data.
        """
        url = urljoin(base_url, f"site/{site_id}/overview")
        params = {'api_key': self.token}

        print("Request URL:", url)
        print("Request Params:", params)
        r = requests.get(url, params=params)
        print("Response:", r.content)
        r.raise_for_status()
        return r.json()

    @staticmethod
    def escape_markdown(text):
        """
        Helper function to escape special characters in MarkdownV2.
        """
        escape_chars = r'\_*[]()~`>#+-=|{}.!'
        return re.sub(
            f"([{re.escape(escape_chars)}])", r'\\\1', text)

    def print_site_overview(self, overview_data):
        overview = overview_data.get('overview')
        if overview:
            overview_str = "Panoramica del sito:\n"
            overview_str += (
                f"Ultimo aggiornamento: {self.escape_markdown(overview.get('lastUpdateTime'))}\n"
                "Dati complessivi:\n"
                f"  Energia: {self.escape_markdown(str(overview['lifeTimeData']['energy']))}\n"
                "Dati ultimo anno:\n"
            )
            last_year_data = overview.get('lastYearData')
            if last_year_data:
                overview_str += (
                    f"  Energia: {self.escape_markdown(str(last_year_data.get('energy')))}\n"
                )
            else:
                overview_str += "  No data available for last year.\n"
            overview_str += "Dati ultimo mese:\n"
            last_month_data = overview.get('lastMonthData')
            if last_month_data:
                overview_str += (
                    f"  Energia: {self.escape_markdown(str(last_month_data.get('energy')))}\n"
                )
            else:
                overview_str += "  No data available for last month.\n"
            overview_str += "Dati per l'ultima giornata:\n"
            last_day_data = overview.get('lastDayData')
            if last_day_data:
                overview_str += (
                    f"  Energia: {self.escape_markdown(str(last_day_data.get('energy')))}\n"
                )
            else:
                overview_str += "  No data available for last day.\n"
            overview_str += "Potenza attuale:\n"
            overview_str += (
                f"  Potenza: {self.escape_markdown(str(overview['currentPower']['power']))}\n"
            )
            return overview_str
        else:
            return "Dati non disponibili."
