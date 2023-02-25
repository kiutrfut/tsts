from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import bot

if name == 'main':
    updater = Updater(token='YOUR_TOKEN', use_context=True)
    dispatcher = updater.dispatcher
    
    start_handler = CommandHandler('start', bot.start)
    dispatcher.add_handler(start_handler)
    
    convert_handler = MessageHandler(Filters.document.video(), bot.convert_video)
    dispatcher.add_handler(convert_handler)
    
    updater.start_polling()
    updater.idle()
