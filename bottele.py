from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Hàm khởi tạo cho lệnh /start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Xin chào! Tôi là bot của bạn.')

# Hàm xử lý tin nhắn
async def echo(update: Update, context: CallbackContext) -> None:
    # Lấy nội dung tin nhắn
    message_text = update.message.text.lower()  # Chuyển thành chữ thường để so sánh không phân biệt hoa thường
    
    # Kiểm tra nội dung tin nhắn và phản hồi tương ứng
    if message_text == "how are you":
        await update.message.reply_text("I am fine")
    else:
        await update.message.reply_text(update.message.text)

# Hàm chính để chạy bot
def main() -> None:
    # Thay thế 'YOUR_TOKEN' bằng mã thông báo của bot bạn
    token = "7103416424:AAHvZT9H7H6bvO8nTmKV31TGi_-PmPusLFU"  # Thay bằng mã thông báo của bạn
    application = Application.builder().token(token).build()

    # Đăng ký handler cho lệnh /start
    application.add_handler(CommandHandler("start", start))

    # Đăng ký handler cho tin nhắn
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Bắt đầu bot
    application.run_polling()

if __name__ == '__main__':
    main()
