import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define the start command handler
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Chào mừng bạn đến với Marketplace Bot! Gõ /market để xem các mục hàng hiện có.')

# Define the market command handler
async def market(update: Update, context: CallbackContext) -> None:
    # Dummy data for market items
    items = [
        {'name': 'Item 1', 'price': '$10', 'description': 'Description for item 1'},
        {'name': 'Item 2', 'price': '$20', 'description': 'Description for item 2'},
        # Add more items as needed
    ]
    
    # Create a response message with the market items
    message = "Các mục hàng hiện có:\n"
    for item in items:
        message += f"Name: {item['name']}\nPrice: {item['price']}\nDescription: {item['description']}\n\n"
    
    await update.message.reply_text(message)

def main() -> None:
    # Your bot's API token
    token = '7103416424:AAHvZT9H7H6bvO8nTmKV31TGi_-PmPusLFU'
    
    # Create the Application and pass it your bot's token
    application = Application.builder().token(token).build()

    # Register handlers for commands
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("market", market))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
