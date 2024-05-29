import logging
import os
import requests
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

logger = logging.getLogger("telegram")


class TelegramHelper:
    def __init__(self):
        self.token = os.getenv("BOT_TOKEN")
        self.chat_id = os.getenv("CHAT_ID").split(",")
        logger.debug("Telegram helper initialized.")

    def __send_telegram_message(self, message: str, chat_id: str):
        url = f'https://api.telegram.org/bot{self.token}/sendMessage'
        data_dict = {
            'chat_id': chat_id,
            'text': message,
            'parse_mode': 'MarkdownV2',
            'disable_notification': True
        }

        logger.debug(f"Sending message to URL: {url}")
        logger.debug(f"Message data: {data_dict}")

        response = requests.post(url, json=data_dict)
        logger.debug(f"Response status: {response.status_code}")
        logger.debug(f"Response content: {response.text}")

        if response.status_code != 200:
            raise Exception(f"Error sending message: {response.text}")

        return response

    def send(self, message):
        for chat_id in self.chat_id:
            self.__send_telegram_message(message, chat_id)
