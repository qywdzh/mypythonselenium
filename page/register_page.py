from base.find_element import FindElement
from util.handle_ini import ini
from util.handle_log import log
import os, sys
from selenium import webdriver
base_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_path)


class RegisterPage(FindElement):
    """
    获取注册页面元素定位
    """
    def __init__(self,driver):
        super().__init__(driver)
        self.note="register"

    def get_email_loc(self):
        """
        获取邮箱输入框定位
        :return:
        """
        key = "email_editor_text"

        email_loc = self.find_element(self.note,key)
        return email_loc



    def get_username_loc(self):
        """
        获取用户名输入框的定位
        :return:
        """
        key = "username_editor_text"
        username_loc = self.find_element(self.note,key)
        return username_loc

    def get_password_loc(self):
        """
        获取密码输入框定位
        :return:
        """
        key = "password_editor_text"
        password_loc = self.find_element(self.note,key)
        return password_loc

    def get_piccode_loc(self):
        """
        获取验证马上输入框定位
        :return:
        """
        key = "piccode_editor_text"
        piccode_loc = self.find_element(self.note,key)
        return piccode_loc

    def get_registerBtn_loc(self):
        """
        获取注册按钮定位
        :return:
        """
        key = "register_button"
        registerBtn_loc = self.find_element(self.note,key)
        return registerBtn_loc

    def get_email_error_msg_loc(self):
        """
        获取email的错误信息定位
        :return:
        """
        key = "email_error_msg"
        email_error_msg_loc = self.find_element(self.note,key)
        return email_error_msg_loc

    def get_username_error_msg_loc(self):
        """
        获取username的错误信息定位
        :return:
        """
        key = "username_error_msg"
        username_error_msg_loc = self.find_element(self.note,key)
        return username_error_msg_loc

    def get_password_error_msg_loc(self):
        """
        获取password的错误信息定位
        :return:
        """
        key = "password_error_msg"
        password_error_msg_loc = self.find_element(self.note,key)
        return password_error_msg_loc

    def get_piccode_error_msg_loc(self):
        """
        获取piccode的错误信息定位
        :return:
        """
        key = "piccode_error_msg"
        piccode_error_msg_loc = self.find_element(self.note,key)
        return piccode_error_msg_loc


if __name__ == '__main__':

    driver = webdriver.Chrome()
    driver.get("http://www.5itest.cn/register")
    el = RegisterPage(driver).get_username_loc().send_keys("111")
    print(el)


