import unittest,os
from selenium import webdriver

base_path = os.path.dirname(os.getcwd())
class StartEnd(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.5itest.cn/register")
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def tearDown(self):
        # filename = base_path + '/report/screenshot/' + "{}.png".format(self._testMethodName)
        for method, error in self._outcome.errors:
            if error:
                filename = base_path + '/report/screenshot/' + "{}.png".format(self._testMethodName)
                self.driver.get_screenshot_as_file(filename)
        # print(filename)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()