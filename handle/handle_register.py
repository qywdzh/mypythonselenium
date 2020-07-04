from page.register_page import RegisterPage
from selenium import webdriver
from util.handle_log import log
import os
base_path = os.path.dirname(os.path.dirname(__file__))






class RegisterHandle(RegisterPage):
    """
    注册页面操作
    """


    def input_email(self,email):
        """
        输入email
        :param email: email账号
        :return:
        """
        log.get_logger().info("输入的邮箱地址位：{}".format(email))
        self.get_email_loc().send_keys(email)

    def input_username(self,username):
        """
        输入username
        :param username: 输入用户名
        :return:
        """
        log.get_logger().info("输入的username为：%s"%username)
        self.get_username_loc().send_keys(username)

    def input_password(self,password):
        """
        输入passwor
        :param password:
        :return:
        """
        log.get_logger().info("输入的password为：{}".format(password))
        self.get_password_loc().send_keys(password)

    def input_piccode(self,code):
        """
        输入图片验证码
        :param code:
        :return:
        """
        log.get_logger().info("图像验证码为：{}".format(code))
        self.get_piccode_loc().send_keys(code)

    def click_registerBtn(self):
        """
        点击"注册"按钮
        :return:
        """
        log.get_logger().info("点击'注册'按钮")
        self.get_registerBtn_loc().click()

    def get_error_msg_text(self,error_msg):
        """
        获取错误信息
        :return:
        """
        # print(type(error_msg))
        try:
            if error_msg == "email_error_msg" :
                error_msg_text = self.get_email_error_msg_loc().text
            elif error_msg == "username_error_msg":
                error_msg_text = self.get_username_error_msg_loc().text
            elif error_msg == "password_error_msg":
                error_msg_text = self.get_password_error_msg_loc().text
            else:
                error_msg_text = self.get_piccode_error_msg_loc().text
        except:
            error_msg_text = None
            log.get_logger().info("error_message:--->{0},error_msg_text--->{1}".format(error_msg,"没有找到类似错误"))
        print(error_msg_text)
        return error_msg_text





if __name__ == '__main__':
    # driver = webdriver.Chrome()
    # driver.get("http://www.5itest.cn/register")
    # RegisterHandle(driver).input_email("1213")
    # RegisterHandle(driver).click_registerBtn()
    # error = RegisterHandle(driver).get_error_msg_text("user_email_error")
    # print(error)
    error_msg = "user_email_error"
    if "user_email_error"==error_msg:
        print(True)

