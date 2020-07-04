from selenium import  webdriver
from base.find_element import FindElement
import time

class ActionMethod():

    def __init__(self,  note, fileName=None):
        self.note = note
        self.fileName = fileName

    def open_browser(self, browser):
        """
        打开浏览器
        :param browser:
        :return:
        """
        if browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "edge":
            self.driver = webdriver.Edge()
        else:
            self.driver = webdriver.Chrome()

    def get_url(self, url):
        """

        :param browser:
        :param url:
        :return:
        """
        self.driver.get(url)

    def close_driver(self, *args):
        """
        关闭driver
        :return:
        """
        self.driver.close()

    def get_title(self):
        """
        获取当前页面的title
        :return:
        """
        title = self.driver.title
        return title

    def element_sleep(self, times):
        """
        设置等待时间
        :return:
        """
        time.sleep(int(times))

    def get_element(self, key):
        """
        获取元素
        :return:
        """
        element = FindElement(self.driver)
        get_element = element.find_element(self.note, key, filename=self.fileName)
        return get_element

    def send_values(self, key, values):
        """
        输入action
        :return:
        """
        self.get_element(key).send_keys(values)

    def click_element(self, key):
        """
        点击action
        :return:
        """
        self.get_element(key).click()




if __name__ == '__main__':
    action = ActionMethod("chrome","register")
    action.get_url("http://www.5itest.cn/register")
    action.element_sleep()
    action.send_values("email_editor_text", "1@1.com")

