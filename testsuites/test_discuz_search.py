import unittest
from testsuites.base_testcase import BaseTestCase
from pageobjects.homepage1 import HomePage
from framework.logger import Logger
import time

logger = Logger(logger = "DiscuzSearch").getlog()

class DiscuzSearch(BaseTestCase):
    def test_homepage1(self):
        h = HomePage(self.driver)
        # h.get_url("http://127.0.0.1/forum.php")
        logger.info("获取网页")
        h.denglu("admin")
        logger.info("登录成功")
        h.fabiao("发表头" , "发表体")
        logger.info("发表成功")
        h.huifu("回复")
        logger.info("回复成功")
        h.tuichu()
        logger.info("退出成功")

    # def test_homepage2(self):
    #     h2 = HomePage2(self.driver)
    #     h2.get_url("http://127.0.0.1/forum.php")
    #     logger.info("获取网页")
    #     h2.guanliyuan("admin")
    #     logger.info("管理员登录成功")
    #     h2.shanchu()
    #     logger.info("删除成功")
    #     h2.tianjia()
    #     logger.info("添加新版块成功")
    #     time.sleep(2)
    #     h2.tuichu()
    #     logger.info("管理员退出成功")
    #     h2.denglu("admin1")
    #     logger.info("普通用户登录成功")
    #     h2.xinbankuai("发表头ssssss","发表体ssssss")
    #     logger.info("普通用户发帖成功")
    #     h2.xinhuifu("新回复sss")
    #     logger.info("普通用户回复成功")
    #
    # def test_homepage3(self):
    #     h3 = HomePage3(self.driver)
    #     h3.get_url("http://127.0.0.1/forum.php")
    #     logger.info("网页获取成功")
    #     h3.denglu("admin")
    #     logger.info("登录成功")
    #     title =h3.sousuo("haotest")
    #     try:
    #         self.assertEqual(title,"haotest",msg=title)
    #         logger.info("断言验证成功")
    #         print(title)
    #     except:
    #         logger.error("断言验证错误")
    #         print("错误")
    #     h3.tuichu()
    #     logger.info("退出成功")
    #
    # def test_homepage4(self):
    #     h4 = HomePage4(self.driver)
    #     h4.get_url("http://127.0.0.1/forum.php")
    #     logger.info("网页获取成功")
    #     h4.denglu("admin")
    #     logger.info("登录成功")
    #     h4.toupiao("投票啊！！！","a","b","c")
    #     logger.info("投票成功")
    #     h4.quchu()
    #     logger.info("取值成功")

if __name__ == "__main__":
    unittest.main()
