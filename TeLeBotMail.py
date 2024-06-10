from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from telegram import Bot, Update
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackContext, Dispatcher
import logging

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
bot_token = 'YOUR_TELEGRAM_BOT_TOKEN'
bot = Bot(token=bot_token)
dispatcher = Dispatcher(bot, None, workers=0)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    telegram_username = db.Column(db.String(50), nullable=False)
    telegram_user_id = db.Column(db.String(50), nullable=False)

db.create_all()

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Welcome! Please link your email using /link <your_email>.')

def link(update: Update, context: CallbackContext):
    if context.args:
        email = context.args[0]
        telegram_username = update.message.from_user.username
        telegram_user_id = update.message.from_user.id

        user = User.query.filter_by(email=email).first()
        if user:
            user.telegram_username = telegram_username
            user.telegram_user_id = telegram_user_id
        else:
            user = User(email=email, telegram_username=telegram_username, telegram_user_id=telegram_user_id)
            db.session.add(user)
        db.session.commit()

        update.message.reply_text(f'Your email {email} has been linked with your Telegram username {telegram_username}.')
    else:
        update.message.reply_text('Please provide your email.')

def find_by_email(update: Update, context: CallbackContext):
    if context.args:
        email = context.args[0]
        user = User.query.filter_by(email=email).first()
        if user:
            update.message.reply_text(f'Telegram Username: {user.telegram_username}')
        else:
            update.message.reply_text('User not found.')
    else:
        update.message.reply_text('Please provide an email.')

def find_by_username(update: Update, context: CallbackContext):
    if context.args:
        telegram_username = context.args[0]
        user = User.query.filter_by(telegram_username=telegram_username).first()
        if user:
            update.message.reply_text(f'Email: {user.email}')
        else:
            update.message.reply_text('User not found.')
    else:
        update.message.reply_text('Please provide a Telegram username.')

def handle_channel_exit(update: Update, context: CallbackContext):
    if update.message.left_chat_member:
        telegram_user_id = update.message.left_chat_member.id
        user = User.query.filter_by(telegram_user_id=telegram_user_id).first()
        if user:
            logging.info(f'User with email {user.email} has left the channel.')

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('link', link))
dispatcher.add_handler(CommandHandler('find_by_email', find_by_email))
dispatcher.add_handler(CommandHandler('find_by_username', find_by_username))
dispatcher.add_handler(MessageHandler(Filters.status_update.left_chat_member, handle_channel_exit))

@app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "OK", 200

if __name__ == '__main__':
    app.run(port=5000)
