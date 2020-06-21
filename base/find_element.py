from selenium import webdriver
from util.handle_ini import ini
from util.handle_log import log
import os
base_path = os.path.dirname(os.getcwd())



class FindElement():



    def __init__(self, driver):

        self.driver = driver


    def find_element(self,note,key,filename=None):
        """
        获取元素定位
        :param note: 所需数据文件的section
        :param key:  所需文件的option
        :param filename: ini文件路径：默认为elementLocal.ini
        :return: 返回元素定位方式
        """
        elementLoc = ini.get_ini(note,key,filename)
        by = elementLoc.split(">")[0]
        value = elementLoc.split(">")[1]
        log.get_logger().info("定位方式：" + by + "定位值：%s"%value )
        try:
            if by == "id":
                return self.driver.find_element_by_id(value)
            elif by == "class_name":
                return self.driver.find_element_by_class_name(value)
            elif by == "name":
                return self.driver.find_element_by_name(value)
            elif by == "tag_name":
                return self.driver.find_element_by_tag_name(value)
            elif by == "xpath":
                return self.driver.find_element_by_xpath(value)
        except:
            return None

    def find_elements(self, note, key, filename=None):
        """
        获取元素定位
        :param note: 所需数据文件的section
        :param key:  所需文件的option
        :param filename: ini文件路径：默认为elementLocal.ini
        :return: 返回元素定位方式
        """
        elementLoc = ini.get_ini(note, key, filename)
        by = elementLoc.split(">")[0]
        value = elementLoc.split(">")[1]
        try:
            if by == "id":
                return self.driver.find_elements_by_id(value)
            elif by == "class_name":
                return self.driver.find_elements_by_class_name(value)
            elif by == "name":
                return self.driver.find_elements_by_name(value)
            elif by == "tag_name":
                return self.driver.find_elements_by_tag_name(value)
            elif by == "xpath":
                return self.driver.find_elements_by_xpath(value)
        except:
            return None


if __name__ == '__main__':
    filename = base_path + '/config/elementLocal.ini'
    # print(filename)
    note = "register"
    key = 'email_editor_text'
    driver = webdriver.Chrome()

    # driver.find_element()
    driver.get("http://wapfront.t1.anmaicloud.com/html/#/register")
    # FindElement(driver).find_element(note,key)
    # loc = tuple(ini.get_ini(note,key))
    # loc2 = ("by","aa")
    # print(type(loc),type(loc2))
    loc = tuple(ini.get_ini(note,key))
    FindElement(driver).find_element(*loc)
    # loc = (By.CLASS_NAME,'mobile')
    # driver.find_element(*loc)
