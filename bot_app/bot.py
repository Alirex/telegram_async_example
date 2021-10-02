from aiogram import Bot, Dispatcher

from config import settings

# Initialize bot and dispatcher
bot = Bot(token=settings.telegram_token)
dp = Dispatcher(bot)
