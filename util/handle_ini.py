import os,sys
base_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_path)
from configparser import ConfigParser



class HandIni():
    """
    操作ini文件
    """

    def load_ini(self,filename=None):
        """
        打开ini文件
        :return:
        """
        if filename:
            filename = base_path + filename
        else:
            filename = base_path + '/config/elementLocal.ini'
        cf = ConfigParser()
        cf.read(filename,encoding="utf-8-sig")
        return cf

    def get_ini(self,note,key,filename=None):
        """
        获取所需的字段
        :return:
        """
        get_value = self.load_ini(filename).get(note,key)
        return get_value


ini = HandIni()
if __name__ == '__main__':
    # filename = base_path + '/config/elementLocal.ini'
    # print(filename)
    note = "register"
    key = 'email_editor_text'
    print(ini.get_ini(note,key))