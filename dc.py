import telegram
from telegram.ext import Updater, CommandHandler
import os
from docx import Document
from moviepy.editor import *

# Define your bot token
bot_token = '5562112612:AAH7Sbz2iIAdoPknjv0FnuiNbiDa_5OFYQA'

# Create an instance of the Updater class
updater = Updater(token=bot_token, use_context=True)

# Get the dispatcher object
dispatcher = updater.dispatcher

# Define the convert command handler function
def convert(update, context):
    # Get the chat ID of the user who sent the message
    chat_id = update.message.chat_id
    # Send a message to the user
    context.bot.send_message(chat_id=chat_id, text="Conversion process started.")

    # Get the file ID of the document to be converted
    file_id = update.message.document.file_id
    # Download the file
    file = context.bot.get_file(file_id)
    file.download()

    # Convert the document to a text file
    document = Document(file.file_path)
    text = ''
    for paragraph in document.paragraphs:
        text += paragraph.text

    # Convert the text file to a video file
    clip = TextClip(text, fontsize=70, color='white', bg_color='black').set_duration(10)
    clip.write_videofile("output.mp4")

    # Send the video file to the user
    context.bot.send_video(chat_id=chat_id, video=open("output.mp4", 'rb'))

    # Delete the downloaded and generated files
    os.remove(file.file_path)
    os.remove("output.mp4")

# Create an instance of the CommandHandler class for the /convert command
convert_handler = CommandHandler('convert', convert)

# Add the command handler to the dispatcher
dispatcher.add_handler(convert_handler)

# Start the bot
updater.start_polling()
