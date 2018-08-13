# -*- coding: UTF-8 -*-
# 基础包：日志服务
import logging
import os
import time


def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.INFO)
    if not logger.handlers:
        log_filename = time.strftime("%Y-%m-%d-%H", time.localtime()) + '.log'
        handler = logging.FileHandler(os.path.join("log/", log_filename))
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        console.setFormatter(formatter)

        logger.addHandler(handler)
        logger.addHandler(console)
    return logger
