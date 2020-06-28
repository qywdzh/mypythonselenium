from base.myunit import StartEnd
from businessView.register_business import RegisterBusiness
import unittest



class RegisterCase(StartEnd):
    """
    注册case
    """

    def test_normal_register(self):
        """正常注册成功"""
        self.assertFalse(RegisterBusiness(self.driver).user_register_success("1@1.com", "qywdzh", "123456", "78778", None))

    def test_email_error(self):
        """email输入错误"""
        self.assertTrue(RegisterBusiness(self.driver).register_email_error("", "qywdzh", "123456", "78778", "email_error_msg"))

    def test_username_error(self):
        """paaword错误"""
        self.assertTrue(RegisterBusiness(self.driver).register_username_error("1@1.com","","123456","78778", "username_error_msg"))

    def test_piccode_error(self):
        """picode错误"""
        self.assertTrue(RegisterBusiness(self.driver).register_piccode_error("1@1.com", "qywdzh", "123456", "78778", "piccode_error_msg"))



if __name__ == '__main__':
    unittest.main()