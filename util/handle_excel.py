import xlrd, os
from xlutils.copy import copy

base_path = os.path.dirname(os.path.dirname(__file__))

class HandleExcel():
    """操作excel"""

    def __init__(self, fileName=None, sheetIndex=None):
        """

        :param fileName: excle文件路径，默认为/config/data.xls
        :param sheetIndex: sheet页的索引，默认为0
        """
        if fileName:
            self.fileName = base_path + fileName
        else:
            self.fileName = base_path + '/config/data.xls'

        if sheetIndex:
            self.sheetIndex = int(sheetIndex)
        else:
            self.sheetIndex = 0

    def open_excel(self):
        """
        打开excel
        :return:
        """
        try:
            excel = xlrd.open_workbook(self.fileName, formatting_info=True)
            return excel
        except:
            error_msg = {"message":"excel打开异常！！"}
            return error_msg

    def get_sheet(self):
        """
        获取sheet数据
        :return:
        """
        try:
            sheet = self.open_excel().sheet_by_index(self.sheetIndex)
            return sheet
        except:
            error_msg = {"message":"sheet页打开异常！！"}

    def get_nrows(self):
        """
        获取数据的总行数
        :return:
        """
        nrows = self.get_sheet().nrows
        if nrows >=1:
            return nrows
        return None

    def get_row_values(self, index):
        """
        获取某一行的数据
        :param index: 所在行的index
        :return:
        """
        if self.get_nrows()> index:
            row_values = self.get_sheet().row_values(index)
            return row_values
        return None

    def get_all_datas(self):
        """
        获取sheet页所有的有效数据
        :return:
        """
        all_datas = []
        nrows = self.get_nrows()
        if nrows:
            [all_datas.append(self.get_row_values(i)) for i in range(1,nrows)]
            return all_datas
        return None

    def write_value(self, row, cols, value):
        """
        将values写入excel
        :param row:
        :param cols:
        :param value:
        :return:
        """
        newWork = copy(self.open_excel())
        newSheet = newWork.get_sheet(0)
        newSheet.write(row, cols, value)
        newWork.save(self.fileName)

    def get_col_values(self, col=None):
        """
        获取制定列的数据
        :param col:
        :return:
        """
        if col:
            col = col
        else:
            col = 0
        col_values = self.get_sheet().col_values(col)
        return col_values

    def get_case_index(self, case_id, col=None):
        """
        通过case_id获取index
        :param case_id:
        :return:
        """
        col_values = self.get_col_values(col)
        for i in range(1, len(col_values)):
            if col_values[i] == case_id:
                return i
        return None

    def get_cell_value(self, row, col):
        """
        获取单元格的数据
        :param row:
        :param col:
        :return:
        """
        if self.get_nrows()>row:
            cell_data = self.get_sheet().cell_value(row, col)
            return cell_data
        return None




if __name__ == '__main__':
    data = HandleExcel().get_row_values(6)
    print(data)


