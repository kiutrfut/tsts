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

# Define function to send a message to a user
def send_message_to_user(chat_id, message):
    try:
        bot.send_message(chat_id=chat_id, text=message)
        logging.info(f"Message sent to user {chat_id}")
    except Exception as e:
        logging.error(f"Error sending message to user {chat_id}: {e}")
