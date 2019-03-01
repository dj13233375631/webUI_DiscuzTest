from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time

class HomePage4(BasePage):
    input_name = (By.NAME, "username")
    input_pwd = (By.NAME, "password")
    button_denglu = (By.CSS_SELECTOR, ".fastlg_l button")

    button_mr = (By.CSS_SELECTOR, ".bm_c td h2 a")

    button_fatie = (By.ID, "newspecial")
    button_toupiao = (By.XPATH, "//ul[@class='tb cl mbw']/li[2]/a")
    input_tpt = (By.NAME, "subject")
    input_xuan1 = (By.CSS_SELECTOR, ".mbm p:nth-child(1) input")
    input_xuan2 = (By.CSS_SELECTOR, ".mbm p:nth-child(2) input")
    input_xuan3 = (By.CSS_SELECTOR, ".mbm p:nth-child(3) input")
    button_fqtp = (By.NAME, "topicsubmit")
    button_dxtp = (By.ID, "option_1")
    button_tijiao = (By.ID, "pollsubmit")

    text_xuan1 = (By.XPATH, "//label[@for='option_1']")
    text_xuan2 = (By.XPATH, "//label[@for='option_2']")
    text_xuan3 = (By.XPATH, "//label[@for='option_3']")

    text_tou1 = (By.CSS_SELECTOR, ".pcht tr:nth-child(2) td:nth-child(2)")
    text_tou2 = (By.CSS_SELECTOR, ".pcht tr:nth-child(4) td:nth-child(2)")
    text_tou3 = (By.CSS_SELECTOR, ".pcht tr:nth-child(6) td:nth-child(2)")
    text_zhuti = (By.CSS_SELECTOR, "h1 span")

    def denglu(self, content):
        self.sendkeys(content, *self.input_name)
        self.sendkeys(content, *self.input_pwd)
        self.click(*self.button_denglu)
        time.sleep(3)
        self.click(*self.button_mr)

    def toupiao(self,content1,content2,content3,content4):
        time.sleep(3)
        self.click(*self.button_fatie)
        self.click(*self.button_toupiao)
        time.sleep(3)
        self.sendkeys(content1, *self.input_tpt)
        self.sendkeys(content2, *self.input_xuan1)
        self.sendkeys(content3, *self.input_xuan2)
        self.sendkeys(content4, *self.input_xuan3)
        time.sleep(3)
        self.click(*self.button_fqtp)
        time.sleep(3)
        self.click(*self.button_dxtp)
        self.click(*self.button_tijiao)
    def quchu(self):
        a = self.text(*self.text_xuan1)
        b = self.text(*self.text_xuan2)
        c = self.text(*self.text_xuan3)
        d = self.text(*self.text_tou1)
        e = self.text(*self.text_tou2)
        f = self.text(*self.text_tou3)
        g = self.text(*self.text_zhuti)
        print("选项：",a,"比例：",d)
        print("选项：",b,"比例：",e)
        print("比例：",c,"比例：",f)
        print("标题：",g)



