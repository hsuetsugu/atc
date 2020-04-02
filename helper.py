import logging
from logging import getLogger, StreamHandler, Formatter, FileHandler
import os
import pandas as pd
from functools import wraps
import time


def elapsed_time(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        v = f(*args, **kwargs)
        print(f'>> {f.__name__}: {time.time() - start:.3}sec')
        return v
    return wrapper


def missing_data(data):
    total = data.isnull().sum()
    percent = (data.isnull().sum() / data.isnull().count() * 100)
    tt = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    types = []
    for col in data.columns:
        dtype = str(data[col].dtype)
        types.append(dtype)
    tt['Types'] = types
    # return np.transpose(tt)
    return tt


def check_and_create_dir(path):
    if not os.path.isdir(path):
        os.mkdir(path)
        print('create directory : {}'.format(path))


def set_logger(fn):
    check_and_create_dir('log')
    LOG = 'log/{:}'.format(fn) + '.log'

    logger = getLogger('__main__')
    logger.setLevel(logging.DEBUG)

    stream_handler = StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    handler_format = Formatter('%(message)s')
    # handler_format = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream_handler.setFormatter(handler_format)
    logger.addHandler(stream_handler)

    handler = FileHandler(LOG, 'a')
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(handler_format)
    logger.addHandler(handler)

    return logger
