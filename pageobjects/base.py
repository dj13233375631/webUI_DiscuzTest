from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger
import time
import os

logger = Logger(logger = "BasePage").getlog()

class BasePage(object):

    def __init__(self,driver):
        self.driver = driver

    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            logger.info("找到页面元素")
        except:
            logger.error("未找到页面元素")




    def click(self,*loc):
        el = self.driver.find_element(*loc)
        el.click()


    # def clear(self,*loc):


    def sendkeys(self,text,*loc):
        el = self.driver.find_element(*loc)
        el.clear()
        el.send_keys(text)


    def get_url(self,url):
        self.driver.get(url)
        logger.info("打开浏览器")

    def jihuo(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        logger.info("激活窗口")


    def text(self ,*loc):
        el = self.driver.find_element(*loc)
        return el.text


    def frame(self, *loc):
        el = self.driver.find_element(*loc)
        self.driver.switch_to.frame(el)

    def clear(self,*loc):
        el = self.driver.find_element(*loc)
        el.clear()





