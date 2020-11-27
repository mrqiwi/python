#!/usr/bin/env python3
# pip install python-telegram-bot
import os
from datetime import datetime
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from telegram.ext import (
    Updater,
    Filters,
    MessageHandler,
    CommandHandler,
    CallbackQueryHandler
)

def button(update, context):
    query = update.callback_query
    query.answer()
    reply = handle_cmd(query.data)
    query.edit_message_text(text=reply)

def print_start(update, context):
    keyboard = [
        [
            InlineKeyboardButton("poweroff", callback_data='poweroff'),
            InlineKeyboardButton("reboot", callback_data='reboot'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)

def print_help(update, context):
    update.message.reply_text( '''Commands list:
                1) poweroff - poweroff, off, выкл, выключение
                2) reboot - reset, reboot, restart, перезагрузка''')

def text(update, context):
    telegram_time = datetime.strptime(str(update.message.date), '%Y-%m-%d %H:%M:%S')
    current_time = datetime.utcnow()
    diff_time = current_time - telegram_time
    # если сообщение было отправлено более 10 сек назад - игнорируем его
    if diff_time.seconds > 10:
        return
    reply = handle_cmd(update.message.text)
    update.message.reply_text(reply)

def handle_cmd(cmd):
    if cmd in ['reset', 'reboot', 'restart', 'перезагрузка']:
        text = 'rebooting...' if os.system('shutdown -r now') == 0 else 'cannot run the command'
        return text

    elif cmd in ['poweroff', 'off', 'выкл', 'выключение']:
        text = 'shutdowing...' if os.system('shutdown -h now') == 0 else 'cannot run the command'
        return text

    else:
        return 'unknown command'

def main():
    updater = Updater(os.getenv('TELETOKEN'), use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CallbackQueryHandler(button))
    dispatcher.add_handler(CommandHandler("start", print_start))
    dispatcher.add_handler(CommandHandler("help", print_help))
    dispatcher.add_handler(MessageHandler(Filters.text, text))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
