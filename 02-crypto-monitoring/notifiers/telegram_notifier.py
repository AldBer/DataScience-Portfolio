from telegram import Bot
from telegram.constants import ParseMode

class TelegramNotifier:
    def __init__(self):
        self.bot = Bot(token=os.environ['TELEGRAM_TOKEN'])
        self.chat_id = os.environ['TELEGRAM_CHAT_ID']
    
    def send(self, message):
        self.bot.send_message(
            chat_id=self.chat_id,
            text=message,
            parse_mode=ParseMode.MARKDOWN
        )