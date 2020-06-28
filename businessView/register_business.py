from handle.handle_register import RegisterHandle


class RegisterBusiness(RegisterHandle):
    """
    注册页面的业务逻辑
    """

    def user_register_common(self, email, username, password, code, error_msg, error_text):
        """
        数据驱动是调用此方法
        :param email:
        :param username:
        :param password:
        :param code:
        :return:
        """
        self.user_register_base(email, username, password, code)
        if error_msg:
            if self.get_error_msg_text(error_msg) == error_text:
                return True
            else:
                return False
        else:
            return True




    def user_register_base(self, email, username, password, code):
        """
        注册操作基础类
        :return:
        """
        self.input_email(email)
        self.input_username(username)
        self.input_password(password)
        self.input_piccode(code)
        self.click_registerBtn()


    def user_register_success(self,email,username,password,code, error_msg):
        """
        成功注册
        :return:
        """
        self.user_register_base(email,username,password,code)
        if self.get_error_msg_text(error_msg):
            return True
        else:
            return False

    def register_email_error(self,email,username,password,code, error_msg):
        """
        email 无效
        :param email:
        :param username:
        :param password:
        :param code:
        :return:
        """
        self.user_register_base(email,username,password,code)
        if self.get_error_msg_text(error_msg):
            return True
        else:
            return False

    def register_username_error(self,email,username,password,code, error_msg):
        """
        username 无效
        :param email:
        :param username:
        :param password:
        :param code:
        :return:
        """
        self.user_register_base(email,username,password,code)
        if self.get_error_msg_text(error_msg):
            return True
        else:
            return False

    def register_password_error(self,email,username,password,code, error_msg):
        """
        password 无效
        :param email:
        :param username:
        :param password:
        :param code:
        :return:
        """
        self.user_register_base(email,username,password,code, error_msg)
        if self.get_error_msg_text(error_msg):
            return True
        else:
            return False

    def register_piccode_error(self,email,username,password,code, error_msg):
        """
        piccode 无效
        :param email:
        :param username:
        :param password:
        :param code:
        :return:
        """
        self.user_register_base(email,username,password,code)
        if self.get_error_msg_text(error_msg):
            return True
        else:
            return False


if __name__ == '__main__':
    pass
