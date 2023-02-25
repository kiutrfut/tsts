import telegram

# Create a bot instance using the bot token
bot = telegram.Bot(token='5562112612:AAH7Sbz2iIAdoPknjv0FnuiNbiDa_5OFYQA')

def start(update, context):
    # Get the chat ID of the user who sent the message
    chat_id = update.message.chat_id
    # Send a message to the user
    bot.send_message(chat_id=chat_id, text="Hello! Welcome to my bot.")

# Create an instance of the telegram.ext.CommandHandler class for the /start command
start_handler = telegram.ext.CommandHandler('start', start)

# Add the command handler to the dispatcher
dispatcher.add_handler(start_handler)
