from telegram import Bot
from telegram.ext import Updater, CommandHandler
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

def fetch_channel_messages(channel_username):
    token = '7103416424:AAHvZT9H7H6bvO8nTmKV31TGi_-PmPusLFU'
    bot = Bot(token=token)
    updates = bot.get_updates()

    # Filter messages from the specific channel
    messages = [update.message.text for update in updates if update.message.chat.username == channel_username]
    return messages

def show_channel_messages(update: Update, context: CallbackContext) -> None:
    channel_username = '5 Phút Crypto Announcement'
    messages = fetch_channel_messages(channel_username)
    response = '\n'.join(messages)
    update.message.reply_text(response)

def main():
    token = '7103416424:AAHvZT9H7H6bvO8nTmKV31TGi_-PmPusLFU'
    updater = Updater(token, use_context=True, update_queue=Queue())

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("market", market))
    dispatcher.add_handler(CommandHandler("channel_messages", show_channel_messages))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
