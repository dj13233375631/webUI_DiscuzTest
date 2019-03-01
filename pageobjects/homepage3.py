from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time

class HomePage3(BasePage):

    input_name = (By.NAME, "username")
    input_pwd = (By.NAME, "password")
    button_denglu = (By.CSS_SELECTOR, ".fastlg_l button")

    input_ss = (By.ID, "scbar_txt")
    button_sousuo = (By.CSS_SELECTOR, ".scbar_btn_td")
    button_haotest = (By.CSS_SELECTOR, ".xs3 a")

    text_title = (By.CSS_SELECTOR, ".ts span")

    button_tc = (By.LINK_TEXT, "退出")

    def denglu(self, content):
        self.sendkeys(content, *self.input_name)
        self.sendkeys(content, *self.input_pwd)
        self.click(*self.button_denglu)

    def sousuo(self,content1):
        time.sleep(2)
        self.sendkeys(content1, *self.input_ss)
        time.sleep(2)
        self.click(*self.button_sousuo)
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.click(*self.button_haotest)
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[2])
        title = self.text(*self.text_title)
        return title




    def tuichu(self):
        time.sleep(3)
        self.click(*self.button_tc)
