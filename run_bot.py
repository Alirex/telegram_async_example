from aiogram import executor

from bot_app import dp
from config.init_logging import init_logging


def main():
    init_logging(is_verbose=True)
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()
