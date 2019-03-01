from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
from framework.logger import Logger
import time

logger = Logger(logger="HomePage").getlog()

class HomePage(BasePage):
    input_name = (By.NAME, "username")
    input_pwd = (By.NAME, "password")
    button_denglu = (By.CSS_SELECTOR, ".fastlg_l button")

    button_mr = (By.CSS_SELECTOR, ".bm_c td h2 a")
    input_title = (By.NAME, "subject")
    input_body = (By.NAME, "message")
    button_ft = (By.NAME, "topicsubmit")

    button_hf = (By.ID, "post_reply")
    input_hfbody = (By.NAME, "message")
    button_cy =(By.ID, "postsubmit")

    button_tc = (By.LINK_TEXT, "退出")

    def denglu(self, content):
        self.sendkeys(content, *self.input_name)
        self.sendkeys(content, *self.input_pwd)
        self.click(*self.button_denglu)
        logger.info("登录")

    def fabiao(self, content1,content2):
        time.sleep(3)
        self.click(*self.button_mr)
        time.sleep(3)
        self.sendkeys(content1, *self.input_title)
        time.sleep(3)
        self.sendkeys(content2, *self.input_body)
        time.sleep(3)
        self.click(*self.button_ft)
        logger.info("发表")

    def huifu(self, content):
        time.sleep(3)
        self.click(*self.button_hf)
        time.sleep(3)
        self.sendkeys(content, *self.input_hfbody)
        time.sleep(3)
        self.click(*self.button_cy)
        logger.info("回复")

    def tuichu(self):
        self.click(*self.button_tc)
        logger.info("退出")







