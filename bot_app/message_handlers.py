import logging
import random

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from config.loggers import get_message_logger
from .bot import dp
from .states import ExampleForm


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """

    # [deep_linking]-[BEGIN]
    # https://t.me/AlirexPrimeEducationBot?start=super_secret_token
    # Also can be used for another commands while chatting
    split = message.text.split(maxsplit=1)
    token = split[1] if len(split) > 1 else None
    # [deep_linking]-[END]

    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")
    if token:
        await message.answer(f'Your token: "{token}"')


# [example_state]-[BEGIN]
@dp.message_handler(commands=['example_state', ])
async def start_state__example_state(message: types.Message):
    # Set current state to this.
    await ExampleForm.name.set()
    await message.reply("What is your name?")


@dp.message_handler(state=ExampleForm.name)
async def example_state__process_name(message: types.Message, state: FSMContext):
    """
    Process user name
    """
    async with state.proxy() as data:
        data['name'] = message.text

        data['some random value'] = random.randint(1, 10)

    await ExampleForm.next()
    await message.reply("How old are you?")


@dp.message_handler(state=ExampleForm.age)
async def example_state__process_age(message: types.Message, state: FSMContext):
    """
    Process user name
    """
    # [validating]-[BEGIN]
    try:
        age = int(message.text)
    except ValueError:
        await message.reply("This must be a number")
        return

    if age <= 0:
        await message.reply("Age must be more then 0")
        return
    # [validating]-[END]

    async with state.proxy() as data:
        data['age'] = message.text

    await ExampleForm.next()
    await message.reply("What is your city?")


@dp.message_handler(state=ExampleForm.city)
async def example_state__process_city(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text

        await message.reply(f"Before finish: {data}")

    await state.finish()

    async with state.proxy() as data:
        await message.reply(f"After finish: {data}")

    await message.reply('end')


# You can use state '*' if you need to handle all states
@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info(f'Cancelling state {current_state}')

    # Cancel state and inform user about it
    await state.finish()
    # And remove keyboard (just in case)
    await message.reply('Cancelled.', reply_markup=types.ReplyKeyboardRemove())


# [example_state]-[END]


@dp.message_handler()
async def echo(message: types.Message):
    logger = get_message_logger()
    logger.info('echo.before')
    await message.answer(message.text)
    await message.reply(message.text)
    logger.info('echo.after')
