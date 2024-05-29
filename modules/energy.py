import requests
from urllib.parse import urljoin

BASEURL = "https://monitoringapi.solaredge.com/site/"


class Energy:
    def __init__(self, token):
        self.token = token

    def get_site_energy(self, SITE_ID, start_date, end_date):
        """
        Get site energy measurements for a specified time period.
        """
        url = urljoin(BASEURL, f"{SITE_ID}/energy")
        params = {
            'api_key': self.token,
            'timeUnit': 'DAY',
            'startDate': start_date,
            'endDate': end_date
        }

        response = requests.get(url, params=params)
        response.raise_for_status()

        try:
            energy_data = response.json()
        except ValueError:
            raise ValueError("Failed to parse response as JSON")

        return energy_data

    def format_energy_data(self, energy_data):
        """
        Format the energy data for display.
        """
        energy = energy_data.get('energy')
        if energy:
            time_unit = energy.get('timeUnit')
            unit = energy.get('unit')
            values = energy.get('values', [])
            formatted_values = "\n".join([
                f"Date: {val['date']}, Energy: {val['value']} {unit}"
                for val in values
            ])
            return (
                f"Time Unit: {time_unit}\n"
                f"Unit: {unit}\n"
                f"Measured By: {energy.get('measuredBy')}\n"
                f"Values:\n{formatted_values}"
            )
        return "No energy data found."
