from aiogram import types

from config.loggers import get_message_logger
from .bot import dp


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    logger = get_message_logger()
    logger.info('echo.before')
    await message.answer(message.text)
    await message.reply(message.text)
    logger.info('echo.after')
