# -*- coding: UTF-8 -*-
# 测试流
import sys
import framework.log as log
import dota2Api as common
from framework import constant
import time
import framework.excel as excel
from prettytable import PrettyTable
filename = constant.FILE_NAME
logging = log.get_logger()

"""1.外部输入API Name"""
path = sys.path[0]      # 当前路径
sheet = sys.argv[1]     # API Name
"""2.根据API Name获取Sheet"""
logging.info("-------------- Execute TestCases ---------------")
excel.open_excel(path + "/" + common.filename)
try:
    sheet = excel.get_sheet(sheet)
except Exception, e:
    logging.error("--------Sheet Name: %s Not Found -----------", sys.argv[1])
    exit()
"""3.执行测试用例"""
rows = excel.get_rows(sheet)
failed = 0
passed = 0
result_table = PrettyTable(["Number", "Description", "Result"])
for i in range(2, rows):
    if excel.get_content(sheet, i, constant.CASE_NUMBER) == '':
        continue
    test_number = int(excel.get_content(sheet, i, constant.CASE_NUMBER))
    if excel.get_content(sheet, i, constant.CASE_DATA) == '':
        test_data = {}
    else:
        test_data = eval(excel.get_content(sheet, i, constant.CASE_DATA))
    # test_data = excel.get_content(sheet, i, constant.CASE_DATA)
    test_status = excel.get_content(sheet, i, constant.CASE_STATUS)
    test_name = excel.get_content(sheet, i, constant.CASE_NAME)
    test_url = excel.get_content(sheet, i, constant.CASE_URL)
    test_method = excel.get_content(sheet, i, constant.CASE_METHOD)
    test_headers = str(excel.get_content(sheet, i, constant.CASE_HEADERS))
    if excel.get_content(sheet, i, constant.EXPECTED) == '':
        expected_result = {}
    else:
        expected_result = eval(excel.get_content(sheet, i, constant.EXPECTED))
    test_status = excel.get_content(sheet, i, constant.CASE_STATUS)

    result = common.run_test(test_method, test_url, test_data, test_headers, expected_result, test_status, test_number)
    if result:
        passed += 1
        result = "Pass"
    else:
        failed += 1
        result = "Failed"
    result_table.align = "l"
    result_table.padding_width = 1
    result_table.add_row([test_number, test_name, result])

time.sleep(1)
print result_table

