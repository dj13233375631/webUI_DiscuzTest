import unittest
import HTMLTestRunner
import os
from testsuites.test_discuz_search import DiscuzSearch
from testsuites.test_discuz_search2 import DiscuzSearch2
from testsuites.test_discuz_search3 import DiscuzSearch3
from testsuites.test_discuz_search4 import DiscuzSearch4

# 设置文件保存路径
# cur_path = os.path.dirname(os.path.realpath(__file__))
# report_path = os.path.join(cur_path,"report")
# if not os.path.exists(report_path):
#     os.mkdir(report_path)

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(DiscuzSearch))
suite.addTest(unittest.makeSuite(DiscuzSearch2))
suite.addTest(unittest.makeSuite(DiscuzSearch3))
suite.addTest(unittest.makeSuite(DiscuzSearch4))

if __name__ == "__main__":

    html_report = r"d:\baidu\report\report.html"
    bg = open(html_report,"wb")

    runner = HTMLTestRunner.HTMLTestRunner(stream=bg,verbosity=2,title="单元测试报告",description="用例执行情况")
    runner.run(suite)