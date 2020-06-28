from selenium import  webdriver
from base.find_element import FindElement
class ActionMethod():
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

    def get_url(self, browser, url):
        """

        :param browser:
        :param url:
        :return:
        """
        self.open_browser(browser).get_url(url)

