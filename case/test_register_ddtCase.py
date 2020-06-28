from base.myunit import StartEnd
from businessView.register_business import RegisterBusiness
from util.handle_excel import HandleExcel
from util.handle_log import log
import unittest, ddt


data = HandleExcel().get_all_datas()
# print(data)
@ddt.ddt()
class RegisterDdtCase(StartEnd):
    """数据驱动"""
    @ddt.data(*data)
    @ddt.unpack
    def test_register(self, case_id, email, username, password, code, error_msg=None, error_text=None, action_result=None):
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
        row = HandleExcel().get_case_index(case_id)
        try:
            self.assertTrue(result)
            HandleExcel().write_value(row, 7, "Pass")
            log.get_logger().info("{}--->test pass !".format(case_id))
        except AssertionError as error_msg:
            HandleExcel().write_value(row, 7, "Fail")
            log.get_logger().info("{}--->test fail !".format(case_id))
            raise error_msg

if __name__ == '__main__':
    unittest.main()