from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from telegram import Update
from config import TOKEN
import function as fu

def start(update: Update, context: CallbackContext):
    first_name = update.message.chat.first_name
    update.message.reply_text(f''' Привет {first_name}. Я тебе рад!

БАЗА ДАННЫХ 1.0

Выбери пункт меню:
/s_db - посмотреть базу данных
/w_db - добавить запись
/c_db - изменить запись
/d_db - удалить запись
    ''')
    fu.init_db('DB.csv')

    message = update.message.text
    if message == '/s_db':
        update.message.reply_text(fu.show_db())
    elif message == '/w_db':
        update.message.reply_text(fu.write_db())
    else:
        update.message.reply_text(f'Введите корректные данные.')


def catch_message(update: Update, context: CallbackContext):
    message = update.message.text
    first_name = update.message.chat.first_name
    if 'привет' in message.lower():
        update.message.reply_text(f'Доброго времени суток {first_name}')
        return None
    update.message.reply_text(f'Я умею повторять: {message}')
    print(message)


updater = Updater(TOKEN)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
answer_handler = MessageHandler(Filters.text, catch_message)
init_db_handler = CommandHandler('s_db', fu.show_db)
write_db_handler = CommandHandler('w_db', fu.write_db)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(answer_handler)
dispatcher.add_handler(init_db_handler)
dispatcher.add_handler(write_db_handler)

print('Началось!')
updater.start_polling()
updater.idle()