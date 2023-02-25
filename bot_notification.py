import os
import logging
import telegram
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Create Telegram bot object
bot = telegram.Bot(token=os.environ.get('5562112612:AAH7Sbz2iIAdoPknjv0FnuiNbiDa_5OFYQA'))

# Define function to send a notification to a group chat
def send_notification_to_group(group_chat_id, message):
    try:
        bot.send_message(chat_id=group_chat_id, text=message)
        logging.info(f"Notification sent to group {group_chat_id}")
    except Exception as e:
        logging.error(f"Error sending notification to group {group_chat_id}: {e}")
