import time
from datetime import datetime, time as dtime
from modules.overview import Overview
import logging
import os

logging.basicConfig(level=logging.DEBUG)
logging.getLogger("main").setLevel(logging.DEBUG)

# Load environment variables
SITE_TOKEN = os.getenv("SITE_TOKEN")
SITE_ID = os.getenv("SITE_ID")
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


class Automate:
    def __init__(self, bot):
        self.bot = bot
        self.interval = 60  # Set the interval to 60 minutes by default
        self.stop_requested = False
        self.overview_api = Overview(SITE_TOKEN)

    def send_automated_messages(self, CHAT_ID):
        try:
            # Send start cycle message
            self.bot.sendMessage(CHAT_ID, "Automated messages started.")

            while not self.stop_requested:
                # Check if current time is within the allowed range
                # (7.00 AM to 9.30 PM)
                current_time = datetime.now().time()
                if dtime(7, 0) <= current_time <= dtime(21, 30):
                    # Get overview data
                    overview_data = self.overview_api.get_site_overview(
                        SITE_ID
                    )
                    overview_message = self.overview_api.print_site_overview(
                        overview_data
                    )

                    # Send overview message
                    self.bot.sendMessage(CHAT_ID, overview_message)
                else:
                    # Send stop cycle message if outside allowed range
                    msg = "Automated messages stopped at 21:30."
                    self.bot.sendMessage(CHAT_ID, msg)
                    self.stop_requested = True

                time.sleep(self.interval * 60)  # Convert minutes to seconds

            # Send stop cycle message
            self.bot.sendMessage(CHAT_ID, "Automated messages stopped.")
        except Exception as e:
            self.bot.sendMessage(CHAT_ID, f"An error occurred: {str(e)}")
