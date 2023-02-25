import os
from telegram import InputFile
from tqdm import tqdm

file_path = "file.mp4"

# Get the file size
file_size = os.path.getsize(file_path)

# Create the InputFile object
input_file = InputFile(file_path)

with tqdm(total=file_size, unit="B", unit_scale=True) as progress_bar:
    # Upload the file in chunks of 10 MB
    for chunk in input_file.iter_chunked(10 * 1024 * 1024):
        # Send the chunk to the chat
        bot.send_video(chat_id=chat_id, video=chunk)
        # Update the progress bar
        progress_bar.update(len(chunk))

print("Upload complete!")
