import telepot
from datetime import datetime
from modules.details import Details
from modules.overview import Overview
from modules.meters import Meters
from modules.production import Production
from modules.energy import Energy
from modules.power import Power
from modules.sensors import Sensors
import logging
import os

logging.basicConfig(level=logging.DEBUG)
logging.getLogger("main").setLevel(logging.DEBUG)

# Load environment variables
SITE_TOKEN = os.getenv("SITE_TOKEN")
SITE_ID = os.getenv("SITE_ID")
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


class MessageHandler:
    def __init__(self, bot, automate_module):
        self.bot = bot
        self.automate_module = automate_module
        self.handlers = {
            "/start": self.handle_start,
            "/help": self.handle_help,
            "/details": self.handle_details,
            "/overview": self.handle_overview,
            "/meters": self.handle_meters,
            "/production": self.handle_production,
            "/energy": self.handle_energy,
            "/power": self.handle_power,
            "/sensors": self.handle_sensors,
            "/automate": self.handle_automate
        }

        # Initialize APIs here if needed
        self.details_api = Details(SITE_TOKEN)
        self.overview_api = Overview(SITE_TOKEN)
        self.meters_api = Meters(SITE_TOKEN, SITE_ID)
        self.production_api = Production(SITE_TOKEN)
        self.energy_api = Energy(SITE_TOKEN)
        self.power_api = Power(SITE_TOKEN)
        self.sensors_api = Sensors(SITE_TOKEN)

    def handle_message(self, msg):
        content_type, _, CHAT_ID = telepot.glance(msg)
        if content_type == 'text':
            command = msg['text']
            if command in self.handlers:
                self.handlers[command](CHAT_ID)
            else:
                msg = "Sorry, I didn't understand that command."
                self.bot.sendMessage(CHAT_ID, msg)
        else:
            msg = "Sorry, I only understand text messages."
            self.bot.sendMessage(CHAT_ID, msg)

    def handle_start(self, CHAT_ID):
        msg = "Welcome to SolarEdge Bot. Type /help to see available commands."
        self.bot.sendMessage(CHAT_ID, "Hello! " + msg)

    def handle_help(self, CHAT_ID):
        help_message = (
            "Available commands:\n"
            "/details - Get site details\n"
            "/overview - Get site overview\n"
            "/meters - Get meter data\n"
            "/production - Get daily production\n"
            "/energy - Get site energy data\n"
            "/power - Get site power data\n"
            "/sensors - Get sensor data\n"
            "/automate - Set up automated notifications\n"
            "/start - Start the bot\n"
            "/help - Show this help message"
        )
        self.bot.sendMessage(CHAT_ID, help_message)

    def handle_details(self, CHAT_ID):
        details = self.details_api.get_details(SITE_ID)
        formatted_details = self.details_api.format_site_details(details)
        self.bot.sendMessage(CHAT_ID, formatted_details)

    def handle_overview(self, CHAT_ID):
        overview_data = self.overview_api.get_site_overview(SITE_ID)
        self.bot.sendMessage(
            CHAT_ID, self.overview_api.print_site_overview(overview_data)
        )

    def handle_meters(self, CHAT_ID):
        meters_data = self.meters_api.get_meter_data()
        self.bot.sendMessage(
            CHAT_ID, self.meters_api.print_meter_data(meters_data)
        )

    def handle_production(self, CHAT_ID):
        start_date = datetime.now().replace(
            hour=0, minute=0, second=0, microsecond=0
        )
        end_date = datetime.now().replace(
            hour=23, minute=59, second=59, microsecond=999
        )
        production_data = self.production_api.get_daily_production(
            start_date, end_date
        )
        self.bot.sendMessage(
            CHAT_ID, self.production_api.print_daily_production(
                production_data
            )
        )

    def handle_energy(self, CHAT_ID):
        start_date = datetime.now().replace(
            hour=0, minute=0, second=0, microsecond=0
        )
        end_date = datetime.now().replace(
            hour=23, minute=59, second=59, microsecond=999
        )
        energy_data = self.energy_api.get_site_energy(
            SITE_ID,
            start_date.strftime('%Y-%m-%d'),
            end_date.strftime('%Y-%m-%d')
        )
        formatted_energy_data = self.energy_api.format_energy_data(energy_data)
        self.bot.sendMessage(CHAT_ID, formatted_energy_data)

    def handle_power(self, CHAT_ID):
        power_data = self.power_api.get_site_power(SITE_ID)
        formatted_power_data = self.power_api.format_power_data(power_data)
        self.bot.sendMessage(CHAT_ID, f"Power data:\n{formatted_power_data}")

    def handle_sensors(self, CHAT_ID):
        sensor_data = self.sensors_api.get_sensor_data(SITE_ID)
        if sensor_data is not None:
            formatted_sensor_data = self.sensors_api.format_sensor_data(
                sensor_data
            )
            self.bot.sendMessage(
                CHAT_ID, f"Sensor data:\n{formatted_sensor_data}"
            )
        else:
            self.bot.sendMessage(CHAT_ID, "No sensor data available.")

    def handle_automate(self, CHAT_ID):
        self.automate_module.interval = 90
        self.automate_module.send_automated_messages(CHAT_ID)
