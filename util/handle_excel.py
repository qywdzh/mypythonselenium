import xlrd, os

base_path = os.path.dirname(os.getcwd())

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
        excel = xlrd.open_workbook(self.fileName)
        return excel

    def get_sheet(self):
        """
        获取sheet数据
        :return:
        """
        sheet = self.open_excel().sheet_by_index(self.sheetIndex)
        return sheet

    def get_nrows(self):
        """
        获取数据的总行数
        :return:
        """
        nrows = self.get_sheet().nrows
        return nrows

    def get_row_values(self, index):
        """
        获取某一行的数据
        :param index: 所在行的index
        :return:
        """
        row_values = self.get_sheet().row_values(index)
        return row_values

    def get_all_datas(self):
        """
        获取sheet页所有的有效数据
        :return:
        """
        all_datas = []
        nrows = self.get_nrows()
        [all_datas.append(self.get_row_values(i)) for i in range(1,nrows)]
        return all_datas


if __name__ == '__main__':
    all_datas = HandleExcel().get_all_datas()
    print(all_datas)

