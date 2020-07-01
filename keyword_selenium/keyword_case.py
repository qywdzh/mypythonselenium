from util.handle_excel import HandleExcel
from keyword_selenium.keyword_action import KeyWordAction


class KeyWordCase():

    def run_main(self):
        self.action = KeyWordAction("register")
        excel = HandleExcel("/config/keyword.xls", 0)
        case_num = excel.get_nrows()
        for i in range(1,case_num):
            is_run = excel.get_cell_value(i, 2)
            handle_method = excel.get_cell_value(i, 3)
            send_keys = excel.get_cell_value(i, 4)
            handle_element = excel.get_cell_value(i, 5)
            excpt_result_method = excel.get_cell_value(i, 6)
            excpt_result = excel.get_cell_value(i, 7)
            if is_run == "yes":
                self.run_method(handle_method, send_keys, handle_element)
                if excpt_result:
                    excpt_result_values = self.get_excpt_result_values(excpt_result)
                    if excpt_result_values[0] == "text":
                        result = self.run_method(excpt_result_method)
                        if self.get_excpt_result_values(excpt_result)[1] in result:
                            excel.write_value(i, 8, "pass")
                        else:
                            excel.write_value(i, 8, "fail")
                    elif self.get_excpt_result_values(excpt_result)[0] == "element":
                        result = self.run_method(excpt_result_method, handle_element=excpt_result_values[1])
                        if result:
                            excel.write_value(i, 8, "pass")
                        else:
                            excel.write_value(i, 8, "fail")
                    else:
                        print("没有else")
                else:
                    print("预期为空")

    def get_excpt_result_values(self, data):
        """

        :param data:
        :return:
        """
        return data.split("=")

    def run_method(self, hamdle_method, send_keys="", handle_element=""):
        action = getattr(self.action, hamdle_method)
        if send_keys != "" and handle_element != "":
            result = action(handle_element, send_keys)
        elif send_keys != "" and handle_element == "":
            result = action(send_keys)
        elif send_keys == "" and handle_element != "":
            result = action(handle_element)
        else:
            result = action()
        return result



if __name__ == '__main__':
    KeyWordCase().run_main()