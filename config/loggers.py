import logging


def get_core_logger() -> logging.Logger:
    return logging.getLogger('Core')


def get_message_logger() -> logging.Logger:
    return logging.getLogger('Message')
