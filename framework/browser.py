from configparser import ConfigParser
from selenium import webdriver
from framework.logger import Logger
import os.path

logger = Logger(logger = "Browser").getlog()

class Browser(object):
    dir = os.path.dirname(os.path.abspath("."))
    gg = dir + "/tools/chromedriver.exe"
    ie = dir + "/tools/IEDriverServer.exe"
    ff = dir + "/tools/geckodriver.exe"

    def open_browser(self):
        config = ConfigParser()
        lj = os.path.dirname(os.path.abspath(".")) + "/config/config.ini"
        config.read(lj)

        browser = config.get("browserType","browserName")
        url = config.get("testServer","URL")

        if browser == "Chrome":
            self.driver = webdriver.Chrome(self.gg)

        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        return self.driver

    def quit_browser(self):
        self.driver.quit()



