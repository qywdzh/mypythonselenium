from base.find_element import FindElement
from selenium import webdriver
from time import sleep


class KeyWordAction():
    """关键词驱动方法"""

    def __init__(self, note, fileName=None):
        self.note = note
        self.fileName = fileName


    def open_browser(self, browser=None):
        """
        获取webdrivr对象
        :param browser:
        :return:
        """
        if isinstance(browser, str):
            browser.lower()
        else:
            try:
                browser = str(browser).lower()
            except:
                error_msg = {"message":"browser类型必须为字符串"}
                return error_msg
        if browser == "edge":
            self.driver = webdriver.Edge()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Chrome()

    def get_url(self, url):
        """
        打开测试地址
        :param url:
        :return:
        """
        self.driver.get(url)

    def element_sleep(self, times):
        """
        强制等待时间
        :param times:
        :return:
        """
        try:
            sleep(int(times))
        except:
            error_msg = {"message":"time不是整型"}

    def get_element(self, elementKey):
        """

        :param key:
        :return:
        """

        element = FindElement(self.driver).find_element(self.note, elementKey, self.fileName)
        return element

    def send_values(self, elementKey, values):
        """
        输入values
        :param elementKey:
        :param values:
        :return:
        """
        self.get_element(elementKey).send_keys(values)

    def element_click(self, elementKey):
        """
        点击行为
        :return:
        """
        self.get_element(elementKey).click()

    def close_browser(self):
        """
        关闭wendriver对象
        :return:
        """
        self.driver.close()



if __name__ == '__main__':
    ky = KeyWordAction('register')
    ky.open_browser()
    ky.get_url("http://www.5itest.cn/register")
    ky.element_sleep(2)
    ky.send_values("email_editor_text", "qywdzh@qq.com")
    ky.close_browser()





