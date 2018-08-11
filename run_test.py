# -*- coding: UTF-8 -*-
# 验证包：接口测试脚本
import sys
import framework.log as log
import base_test as common
logging = log.get_logger()


"""1.外部输入参数"""
path = sys.path[0]      # 当前路径
module = "Sheet1"         # 服务模块名
# url = sys.argv[2]       # 服务地址
"""2.根据module获取Sheet"""
logging.info("-------------- Execute TestCases ---------------")
sheet = common.get_excel_sheet(path + "/" + common.filename, module)
"""3.执行测试用例"""
res = common.run_test(sheet)
logging.info("-------------- Get the result ------------ %s", res)
"""这里的res是我们平滑升级的时候需要返回结果为TRUE才会继续下面走。"""