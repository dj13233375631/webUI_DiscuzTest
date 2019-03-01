import unittest
from testsuites.base_testcase import BaseTestCase
from pageobjects.homepage4 import HomePage4
from framework.logger import Logger
import time
logger = Logger(logger = "DiscuzSearch4").getlog()
class DiscuzSearch4(BaseTestCase):
    def test_homepage4(self):
        h4 = HomePage4(self.driver)
        # h4.get_url("http://127.0.0.1/forum.php")
        logger.info("网页获取成功")
        h4.denglu("admin")
        logger.info("登录成功")
        h4.toupiao("投票啊！！！","a","b","c")
        logger.info("投票成功")
        h4.quchu()
        logger.info("取值成功")

if __name__ == "__main__":
    unittest.main()