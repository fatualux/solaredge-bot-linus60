import logging
import os
from modules.tg_helper import TelegramHelper
from modules.overview import Overview

logging.basicConfig(level=logging.DEBUG)
logging.getLogger("main").setLevel(logging.DEBUG)

# Load environment variables
SITE_TOKEN = os.getenv("SITE_TOKEN")
SITE_ID = os.getenv("SITE_ID")
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

telegram_helper = TelegramHelper()

# Initialize overview API
overview_api = Overview(SITE_TOKEN)

try:
    # Get site overview
    overview_data = overview_api.get_site_overview(SITE_ID)
    overview_message = overview_api.print_site_overview(overview_data)

    # Send the overview message via Telegram
    telegram_helper.send(overview_message)
except Exception as e:
    logging.error(f"Error in main execution: {e}")
