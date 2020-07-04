from util.handle_excel import HandleExcel
from keyword_selenium.actionMethod import ActionMethod

class RunKeyWordCase():
    """关键词驱动run文件"""
    def run_main(self):
        self.action = ActionMethod("register")
        excel  = HandleExcel('/config/keyword.xls', 0)
        case_lines = excel.get_nrows()
        if case_lines:
            for i in range(1,case_lines):
                is_run = excel.get_cell_value(i, 2)
                if is_run == "yes":
                    hand_method = excel.get_cell_value(i, 4)
                    send_values = excel.get_cell_value(i, 5)
                    handle_element = excel.get_cell_value(i, 6)
                    except_result_method = excel.get_cell_value(i, 7)
                    except_result = excel.get_cell_value(i, 8)
                    # print(except_result)
                    self.run_method(hand_method, send_values, handle_element)
                    if except_result != "":
                        except_values = self.get_except_result(except_result)
                        # print(except_values)
                        if except_values[0] == "text":
                            result = self.run_method(except_result_method)
                            if except_values[1] in result:
                                excel.write_value(i, 9, "pass")
                            else:
                                excel.write_value(i, 9, "fail")
                        elif except_values[0] == "element":
                            # print(except_values[1])
                            result = self.run_method(except_result_method, except_values[1])
                            if result:
                                excel.write_value(i, 9, "pass")
                            else:
                                excel.write_value(i, 9, "fail")
                        else:
                            print("既不是text也不是element")
                    else:
                        print("不用断言")


    def get_except_result(self, data):
        """
        获取预期的规则
        :param data:
        :return:
        """
        return data.split("=")

    def run_method(self, handle_method, send_values="", handle_element=""):
        """run method 的逻辑"""
        action_method = getattr(self.action, handle_method)
        if send_values != "" and handle_element != "":
            result = action_method(handle_element, send_values)
        elif send_values != "" and handle_element == "":
            result = action_method(send_values)
        elif send_values == "" and handle_element != "":
            result = action_method(handle_element)
        else:
            result = action_method()

        return result




if __name__ == '__main__':
    data = RunKeyWordCase().run_main()
