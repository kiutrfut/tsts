import subprocess
from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackContext

def status(update: Update, context: CallbackContext) -> None:
    # Get the chat ID of the user who sent the message
    chat_id = update.message.chat_id

    # Get the output of the "ps" command to find the processes running ffmpeg
    ps = subprocess.Popen(('ps', 'aux'), stdout=subprocess.PIPE)
    output = subprocess.check_output(('grep', 'ffmpeg'), stdin=ps.stdout)
    ps.wait()

    # If there are no ffmpeg processes running, send a message indicating that there are no downloads or uploads in progress
    if not output:
        context.bot.send_message(chat_id=chat_id, text="There are no downloads or uploads in progress.")
        return

    # Otherwise, send a message indicating the current status of each ffmpeg process
    message = "*Downloads and uploads in progress:*\n"
    for line in output.splitlines():
        fields = line.decode().split()
        pid = fields[1]
        cmd = " ".join(fields[10:])
        message += f"{pid} {cmd}\n"

    context.bot.send_message(chat_id=chat_id, text=message, parse_mode=ParseMode.MARKDOWN)

# Create an instance of the Updater class
updater = Updater(token='5562112612:AAH7Sbz2iIAdoPknjv0FnuiNbiDa_5OFYQA', use_context=True)

# Get the dispatcher object
dispatcher = updater.dispatcher

# Create an instance of the CommandHandler class for the /status command
status_handler = CommandHandler('status', status)

# Add the command handler to the dispatcher
dispatcher.add_handler(status_handler)

# Start the bot
updater.start_polling()
