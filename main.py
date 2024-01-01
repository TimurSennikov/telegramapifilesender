from telegram import Update                                                                    
from telegram.ext import Application, MessageHandler, filters, ContextTypes, CommandHandler
import os
import logging
import time
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

FILES = "/home/timur/camera"
TOKEN = "your bot token"
SKIBIDI = "dop dop dop"

files = [f for f in os.listdir(FILES) if os.path.isfile(os.path.join(FILES, f))]

async def getallfiles(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    for i, file in enumerate(files, start=1):
        fileinlist = str(i) + " " + file
        await context.bot.send_message(chat_id=update.message.chat_id, text=fileinlist)

async def send_file(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        selection = int(user_input)
        if 1 <= selection <= len(files):
            selected_file = files[selection - 1]
            file_path = os.path.join(FILES, selected_file)
            with open(file_path, "rb") as file:
                await context.bot.send_document(chat_id=update.message.chat_id, document=file)
        else:
            await context.bot.send_message(chat_id=update.message.chat_id, text="Invalid selection.")

async def input_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global user_input
    input_value = context.args[0] if context.args else None

    if input_value:
        user_input = input_value
        await update.message.reply_text(f"Input set to: {user_input}")
    else:
        await update.message.reply_text("Please provide a valid input.")

def main() -> None:                                                                            
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("listallfiles", getallfiles))
    application.add_handler(CommandHandler("input", input_command))
    application.add_handler(CommandHandler("sendfile", send_file))

    application.run_polling(allowed_updates=Update.ALL_TYPES)
if __name__ == "__main__":
    main()
