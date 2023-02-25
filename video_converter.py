import os
import urllib.request
from pyrogram import Client, filters
from pyrogram.types import Message
import ffmpeg

# Telegram API credentials
api_id = YOUR_API_ID
api_hash = 'YOUR_API_HASH'
bot_token = 'YOUR_BOT_TOKEN'

# Output format to convert to
output_format = "mp4"

# Create a Pyrogram client instance
app = Client("FileConverterBot", api_id, api_hash, bot_token=bot_token)

# Handler function to handle file conversion requests
@app.on_message(filters.private & filters.document)
async def handle_conversion_request(client, message: Message):
    # Get file information from the message
    file_id = message.document.file_id
    file_name = message.document.file_name

    # Download the file
    file_path = await message.download()

    # Construct output file path
    output_file_name = os.path.splitext(file_name)[0] + "." + output_format
    output_file_path = os.path.join(os.path.dirname(file_path), output_file_name)

    try:
        # Convert the file using ffmpeg
        (
            ffmpeg
            .input(file_path)
            .output(output_file_path)
            .run()
        )

        # Upload the converted file
        await client.send_document(message.chat.id, document=output_file_path)

    except Exception as e:
        # Handle any errors that occur during file conversion
        print(e)
        await message.reply_text("Sorry, there was an error during file conversion.")
    
    # Clean up the input and output files
    os.remove(file_path)
    os.remove(output_file_path)

# Start the client and run the bot
app.run()
