from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import settings

# Initialize bot
bot = Bot(token=settings.telegram_token)

# Create storage for Finite State Machine
# More storages here:
#   https://docs.aiogram.dev/en/latest/dispatcher/fsm.html
storage = MemoryStorage()

# Initialize dispatcher
dp = Dispatcher(bot, storage=storage)
