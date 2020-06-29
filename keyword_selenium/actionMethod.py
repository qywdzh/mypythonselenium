from selenium import  webdriver
from base.find_element import FindElement
import time

class ActionMethod():

    def __init__(self, browser, note, key, fileName=None):
        self.driver = self.open_browser(browser)
        self.element = FindElement(self.driver)
        self.note = note
        self.key = key
        self.fileName = fileName

    def open_browser(self, browser):
        """
        打开浏览器
        :param browser:
        :return:
        """
        if browser == "firefox":
            driver = webdriver.Firefox()
        elif browser == "edge":
            driver = webdriver.Edge()
        else:
            driver = webdriver.Chrome()
        return driver

    def get_url(self, url):
        """

        :param browser:
        :param url:
        :return:
        """
        self.driver.get(url)

    def element_sleep(self):
        """
        设置等待时间
        :return:
        """
        time.sleep(2)

    def get_element(self):
        """
        获取元素
        :return:
        """
        get_element = self.element.find_element(self.note, self.key, filename=self.fileName)
        return get_element

    def send_values(self, values):
        """
        输入action
        :return:
        """
        self.get_element().send_keys(values)

    def click_element(self):
        """
        点击action
        :return:
        """
        self.get_element().click()

