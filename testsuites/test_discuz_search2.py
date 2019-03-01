import unittest
from testsuites.base_testcase import BaseTestCase
from pageobjects.homepage2 import HomePage2
from framework.logger import Logger
import time
logger = Logger(logger = "DiscuzSearch2").getlog()
class DiscuzSearch2(BaseTestCase):
    def test_homepage2(self):
        h2 = HomePage2(self.driver)
        # h2.get_url("http://127.0.0.1/forum.php")
        logger.info("获取网页")
        h2.guanliyuan("admin")
        logger.info("管理员登录成功")
        h2.shanchu()
        logger.info("删除成功")
        h2.tianjia()
        logger.info("添加新版块成功")
        time.sleep(2)
        h2.tuichu()
        logger.info("管理员退出成功")
        h2.denglu("admin1")
        logger.info("普通用户登录成功")
        h2.xinbankuai("发表头ssssss111","发表体ssssss111")
        logger.info("普通用户发帖成功")
        h2.xinhuifu("新回复sss1111111")
        logger.info("普通用户回复成功")

if __name__ == "__main__":
    unittest.main()