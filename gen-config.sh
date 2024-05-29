#!/bin/bash

CONFIG_FILE="secrets.sh"

echo -n "Enter your Solaredge's token: "
read -r SITE_TOKEN
echo -n "Enter your Solaredge's site id: "
read -r SITE_ID
echo -n "Enter your Telegram bot token: "
read -r BOT_TOKEN
echo -n "Enter your Telegram chat id(s) (comma-separated): "
read -r CHAT_ID

cat <<EOL > $CONFIG_FILE
export SITE_TOKEN='$SITE_TOKEN'
export SITE_ID='$SITE_ID'
export BOT_TOKEN='$BOT_TOKEN'
export CHAT_ID='$CHAT_ID'
EOL

echo "Configuration written to $CONFIG_FILE."
