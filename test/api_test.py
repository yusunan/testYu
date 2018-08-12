# -*- coding: UTF-8 -*-
# 基础包：日志服务
import requests
import framework.log as log
logging = log.get_logger()


def get_response(method, url, data, headers):
    try:
        if method == "post":
            results = requests.post(url, data, headers=headers)
        if method == "get":
            results = requests.get(url, data, headers=headers)
        if method == "put":
            results = requests.put(url, data, headers=headers)
        if method == "delete":
            results = requests.delete(url, headers=headers)
        if method == "patch":
            results == requests.patch(url, data, headers=headers)
        if method == "options":
            results == requests.options(url, headers=headers)
        return results
    except Exception, e:
        logging.error("service is error", e)
