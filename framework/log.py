# -*- coding: UTF-8 -*-
# 基础包：日志服务
import logging
import time

def get_logger():
    global log_path
    try:
        log_path
    except NameError:
        log_path = "/data/log/apiTest/"
    FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    # file = tezLogPath + time.strftime("%Y-%m-%d", time.localtime()) + ".log"
    # logging.basicConfig(filename=file, level=logging.INFO, format=FORMAT)
    # 开发阶段为了方便调试，可不输出到文件
    logging.basicConfig(level=logging.INFO, format=FORMAT)
    return logging
