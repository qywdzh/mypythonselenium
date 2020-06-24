from base.myunit import StartEnd
from businessView.register_business import RegisterBusiness
from util.handle_excel import HandleExcel
import unittest, os, sys, ddt
base_path = os.path.dirname(os.getcwd())
sys.path.append(base_path)

data = HandleExcel().get_all_datas()

@ddt.ddt()
class RegisterDdtCase(StartEnd):
    """数据驱动"""
    @ddt.data(*data)
    @ddt.unpack
    def test_register(self, email, username, password, code, error_msg=None, error_text=None):
        """
        数据驱动case
        :param email:
        :param username:
        :param password:
        :param code:
        :param error_msg:
        :param error_text:
        :return:
        """
        result = RegisterBusiness(self.driver).user_register_common(email, username, password, code, error_msg, error_text)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()