from bot.bot import Bot
from bot.handler import MessageHandler

TOKEN = "001.3711403680.1890224372:756211742"

botId = 756211742

nick = "hutoryanin_bot"


bot = Bot(token=TOKEN, poll_time_s=15)


def message_cb(bot, event):
    bot.send_text(chat_id=event.from_chat, text=event.text)


bot.dispatcher.add_handler(MessageHandler(callback=message_cb))
bot.stop()

#bot.start_polling()
#bot.idle()

