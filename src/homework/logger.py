import os
import logging


def return_path():
    return os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'logs')


def setup_logging(logger_name, file_name):
    log_dir = return_path()
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False
    file_handler = logging.FileHandler(os.path.join(log_dir, file_name), mode='w', encoding='utf-8')
    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
