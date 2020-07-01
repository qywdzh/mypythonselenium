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


    def run_method(self, hamdle_method, send_keys, handle_element):
        action = getattr(self.action, hamdle_method)
        if send_keys != "" and handle_element != "":
            action(send_keys, handle_element)
        elif send_keys != "" and handle_element == "":
            action(send_keys)
        elif send_keys == "" and handle_element != "":
            action(handle_element)
        else:
            action()


