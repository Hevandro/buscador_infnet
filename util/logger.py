# -*- coding: utf-8 -*-

import logging
from functools import wraps
from time import time

def logger(log_path):       
    def wrap(f):
        @wraps(f)
        def decorator(*args, **kw):
            #codigo antes
            log(f.__qualname__, log_path)
           
            log_gen = logging.getLogger(f.__qualname__)
            
            #g_gen = logging.getLogger(f.__name__)
            message = 'Starting function...'
            log_gen.info(message)
            
            ts = time()
            result = f(*args, **kw)
            #codigo depois
            elapsed_time = time() - ts
            message = 'Finished function, took: {:2.4f}'.format(elapsed_time)
            log_gen.info(message)
            
            return result
        return decorator
    return wrap

def log(name, logFile):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    if not len(logger.handlers):
        # create a file handler
        handler = logging.FileHandler(logFile)
        handler.setLevel(logging.INFO)
        # create a logging format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(formatter)
        # add the handlers to the logger
        logger.addHandler(handler)
        logger.addHandler(streamHandler) 