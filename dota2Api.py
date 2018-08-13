# -*- coding: UTF-8 -*-
# 业务包：通用函数
import framework.log as log
from framework import constant
import test.api_test as request
filename = constant.FILE_NAME
logging = log.get_logger()


def run_test(test_method, test_url, test_data, test_headers, expected_result, test_status, test_number):
    """Response"""
    response = request.get_response(test_method, test_url, test_data, test_headers)
    actual_code = response.status_code
    expect_code = int(test_status)
    """Check Status"""
    if actual_code == expect_code:
        logging.info("--------Number: %s Check status passed--------", test_number)
    else:
        logging.error("--------Number: %s Check status code failed------Expect: %s, But found: %s", test_number, expect_code, actual_code)
        return False
    """Check Body"""
    if check_body(response, expected_result):
        logging.info("--------Number: %s Check body passed--------", test_number)
    else:
        logging.error("--------Number: %s Check body failed------", test_number)
        return False
    return True


def check_body(response, expected_result):
    if response.status_code == 200:
        response = response.json()['result']
    else:
        response = response.text
    for key, value in expected_result.items():
        if value == 'any':
            response[key] = 'any'
        try:
            if response[key] != value:
                logging.error("--------Check body failed------Expect: %s, But found: %s", value, response[key])
                return False
        except KeyError:
            logging.error("--------Check body failed------Key not found: %s", key)
            return False

    return True
