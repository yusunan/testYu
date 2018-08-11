# -*- coding: UTF-8 -*-
# 业务包：通用函数
import framework.log as log
import constant
import framework.excel as excel
import test.api_test as request
from prettytable import PrettyTable
filename = constant.FILE_NAME
logging = log.get_logger()


def get_excel_sheet(path, module):
    """依据模块名获取sheet"""
    excel.open_excel(path)
    return excel.get_sheet(module)


def run_test(sheet):
    """再执行测试用例"""
    rows = excel.get_rows(sheet)
    fail = 0
    for i in range(2, rows):
        test_number = str(excel.get_content(sheet, i, constant.CASE_NUMBER))
        test_data = excel.get_content(sheet, i, constant.CASE_DATA)
        test_name = excel.get_content(sheet, i, constant.CASE_NAME)
        test_url = excel.get_content(sheet, i, constant.CASE_URL)
        # test_url = url + test_url
        test_method = excel.get_content(sheet, i, constant.CASE_METHOD)
        test_headers = str(excel.get_content(sheet, i, constant.CASE_HEADERS))
        # test_headers = eval(replace_holder(test_headers))
        test_code = excel.get_content(sheet, i, constant.CASE_CODE)
        actual_code = request.api_test(test_method, test_url, test_data, test_headers)
        expect_code = int(test_code)
        fail_results = PrettyTable(["Number", "Method", "Url", "Data", "ActualCode", "ExpectCode"])
        fail_results.align["Number"] = "l"
        fail_results.padding_width = 1
        fail_results.add_row([test_number, test_method, test_url, test_data, actual_code, expect_code])
        if actual_code != expect_code:
            logging.info("FailCase %s", test_name)
            print "FailureInfo"
            print fail_results
            fail += 1
        else:
            logging.info("Number %s", test_number)
            logging.info("TrueCase %s", test_name)
    if fail > 0:
        return False
    return True
