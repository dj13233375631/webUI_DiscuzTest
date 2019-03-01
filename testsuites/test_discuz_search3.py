import unittest
from testsuites.base_testcase import BaseTestCase
from pageobjects.homepage3 import HomePage3
from framework.logger import Logger
import time
logger = Logger(logger = "DiscuzSearch3").getlog()
class DiscuzSearch3(BaseTestCase):
    def test_homepage3(self):
        h3 = HomePage3(self.driver)
        # h3.get_url("http://127.0.0.1/forum.php")
        logger.info("网页获取成功")
        h3.denglu("admin")
        logger.info("登录成功")
        title =h3.sousuo("haotest")
        try:
            self.assertEqual(title,"haotest",msg=title)
            logger.info("断言验证成功")
            print(title)
        except:
            logger.error("断言验证错误")
            print("错误")
        h3.tuichu()
        logger.info("退出成功")

if __name__ == "__main__":
    unittest.main()