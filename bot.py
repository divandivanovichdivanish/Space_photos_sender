import telegram
import os
from dotenv import load_dotenv


load_dotenv()
telegram_token = os.environ["TG_TOKEN"]
bot = telegram.Bot(token=telegram_token)
bot.send_message(chat_id="@beautifulphotosofspace", text="This is a test message")
