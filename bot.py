import os
from telegram import ChatAction
from telegram.ext import ConversationHandler
from moviepy.editor import VideoFileClip

ENTER_FILE = range(1)

def start(update, context):
    update.message.reply_text('Welcome to the video converter bot!')

def convert_video(update, context):
    chat_id = update.message.chat_id
    file = context.bot.get_file(update.message.document.file_id)
    file_name = update.message.document.file_name
    file_extension = os.path.splitext(file_name)[1].lower()
    
    if file_extension != '.mp4':
        context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
        update.message.reply_text('Converting file, please wait...')
        
        with file.download() as f:
            video = VideoFileClip(f.name)
            video_name = os.path.splitext(file_name)[0] + '.mp4'
            video.write_videofile(video_name, codec='libx264', audio_codec='aac')
        
        with open(video_name, 'rb') as f:
            context.bot.send_video(chat_id=chat_id, video=f)
        
        os.remove(video_name)
        
    else:
        context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
        update.message.reply_text('File is already in MP4 format!')
        
    return ConversationHandler.END
