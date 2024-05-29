import telepot
from modules.message_handler import MessageHandler
from modules.automate import Automate
from modules.overview import Overview
from modules.production import Production
import logging
import os

logging.basicConfig(level=logging.DEBUG)
logging.getLogger("main").setLevel(logging.DEBUG)

# Load environment variables
SITE_TOKEN = os.getenv("SITE_TOKEN")
SITE_ID = os.getenv("SITE_ID")
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Initialize the Telegram bot
bot = telepot.Bot(BOT_TOKEN)

# Initialize overview and production APIs
overview_api = Overview(SITE_TOKEN)
production_api = Production(SITE_TOKEN)

# Initialize Automate with bot
automate_module = Automate(bot)

# Initialize MessageHandler with Automate module
message_handler = MessageHandler(bot, automate_module)


# Function to handle incoming messages
def handle(msg):
    message_handler.handle_message(msg)


# Start listening for messages
bot.message_loop(handle)

# Keep the script running
while True:
    pass
