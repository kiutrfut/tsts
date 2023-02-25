import telegram
from telegram.ext import Updater, CommandHandler

# Define your bot token
bot_token = '5562112612:AAH7Sbz2iIAdoPknjv0FnuiNbiDa_5OFYQA'

# Create an instance of the Updater class
updater = Updater(token=bot_token, use_context=True)

# Get the dispatcher object
dispatcher = updater.dispatcher

# Define the start command handler function
def start(update, context):
    # Get the chat ID of the user who sent the message
    chat_id = update.message.chat_id
    # Send a message to the user
    context.bot.send_message(chat_id=chat_id, text="Hello! Welcome to my bot.")

# Create an instance of the CommandHandler class for the /start command
start_handler = CommandHandler('start', start)

# Add the command handler to the dispatcher
dispatcher.add_handler(start_handler)

# Start the bot
updater.start_polling()
