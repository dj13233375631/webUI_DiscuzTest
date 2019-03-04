from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time

class HomePage2(BasePage):
    input_name = (By.NAME, "username")
    input_pwd = (By.NAME, "password")
    button_denglu = (By.CSS_SELECTOR, ".fastlg_l button")

    button_mr = (By.CSS_SELECTOR, "td h2 a")
    button_dj = (By.CSS_SELECTOR, "tbody:nth-last-child(2) tr td:nth-child(2) input")
    button_sc = (By.LINK_TEXT, "删除")
    button_qr = (By.ID, "modsubmit")

    button_gl = (By.LINK_TEXT, "管理中心")
    input_mm = (By.NAME, "admin_password")
    button_tj = (By.NAME, "submit")
    button_lt = (By.LINK_TEXT, "论坛")
    iframe = (By.TAG_NAME, "iframe")
    button_tianjia = (By.CSS_SELECTOR, ".lastboard a")
    button_tijiao = (By.ID,"submit_editsubmit")

    button_zdsy = (By.CSS_SELECTOR, ".btnlink a")

    button_tc = (By.CSS_SELECTOR, ".uinfo a:nth-child(2)")
    button_tuichu = (By.LINK_TEXT, "退出")

    button_xft = (By.CSS_SELECTOR, "tr:nth-child(2) td h2 a")

    input_title = (By.NAME, "subject")
    input_body = (By.NAME, "message")
    button_ft = (By.NAME, "topicsubmit")

    button_hf = (By.ID, "post_reply")
    input_hfbody = (By.NAME, "message")
    button_cy = (By.ID, "postsubmit")


    def guanliyuan(self,content):
        self.sendkeys(content, *self.input_name)
        self.sendkeys(content, *self.input_pwd)
        self.click(*self.button_denglu)

    def shanchu(self):
        time.sleep(3)
        self.click(*self.button_mr)
        time.sleep(3)
        self.click(*self.button_dj)
        time.sleep(3)
        self.click(*self.button_sc)
        time.sleep(3)
        self.click(*self.button_qr)

    def tianjia(self,content):
        self.click(*self.button_gl)
        # window = self.driver.current_window_handle
        # self.driver.switch_to.window(window)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(3)
        try:
            self.sendkeys(content, *self.input_mm)
            time.sleep(3)
            self.click(*self.button_tj)
            time.sleep(3)
        except:
            pass
        self.click(*self.button_lt)
        time.sleep(2)
        self.frame(*self.iframe)
        time.sleep(3)
        self.click(*self.button_tianjia)
        time.sleep(3)
        self.click(*self.button_tijiao)
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.click(*self.button_tc)
        self.driver.switch_to.window(self.driver.window_handles[1])

    def tuichu(self):
        self.click(*self.button_tuichu)

    def denglu(self, content):
        self.sendkeys(content, *self.input_name)
        self.sendkeys(content, *self.input_pwd)
        self.click(*self.button_denglu)

    def xinbankuai(self,content1,content2):
        time.sleep(3)
        self.click(*self.button_xft)
        time.sleep(3)
        self.sendkeys(content1, *self.input_title)
        time.sleep(3)
        self.sendkeys(content2, *self.input_body)
        time.sleep(3)
        self.click(*self.button_ft)

    def xinhuifu(self,content):
        time.sleep(3)
        self.click(*self.button_hf)
        time.sleep(3)
        self.sendkeys(content, *self.input_hfbody)
        time.sleep(3)
        self.click(*self.button_cy)
