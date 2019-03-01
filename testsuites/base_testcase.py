from framework.browser import Browser
from selenium import webdriver
import unittest


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = Browser()
        self.driver = self.browser.open_browser()
        # self.driver = webdriver.Chrome("../tools/chromedriver")
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(3)

    def tearDown(self):
        # pass
        self.driver = self.browser.quit_browser()
