# -*- coding: UTF-8 -*-
# 基础包：日志服务
import requests
import framework.log as log
logging = log.get_logger()


def api_test(method, url, data, headers):
    """
    定义一个请求接口的方法和需要的参数 
    :Args:
    method  - 企业名称 str
    url - 用户昵称 str
    data - 参数 str
    headers - 请求头信息 dict
    非RESTful API请求另外的请求类型实际用不到。也不安全。
    """  
    try:
        if method == "post":
            results = requests.post(url, data, headers=headers)
        if method == "get":
            results = requests.get(url)
        if method == "put":
            results = requests.put(url, data, headers=headers)
        if method == "delete":
            results = requests.delete(url, headers=headers)
        if method == "patch":
            results == requests.patch(url, data, headers=headers)
        if method == "options":
            results == requests.options(url, headers=headers)
        response = results.json()
        code = results.status_code
        return code
    except Exception, e:
        logging.error("service is error", e)
