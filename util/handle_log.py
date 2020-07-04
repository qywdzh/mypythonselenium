import os,sys,logging,time
import logging.config
base_path = os.path.dirname(os.path.dirname(__file__))
# print(base_path)
# sys.path.append(base_path)


class HandleLog():
    """
    操作日志
    """
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        Format = logging.Formatter("[%(asctime)s] [%(filename)s] [lineno:%(lineno)d] [leve:%(levelname)s] [message:%(message)s]","%Y-%m-%d %H:%M:%S")
        #控制台输出
        consle = logging.StreamHandler()
        consle.setLevel(logging.INFO)
        consle.setFormatter(Format)

        #输入值文件

        now = time.strftime("%Y-%m-%d")
        filename = base_path + '/log/' + now + ".log"
        # print(filename)
        file_handler = logging.FileHandler(filename, mode="a", encoding="utf-8-sig")
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(Format)
        self.logger.addHandler(consle)
        self.logger.addHandler(file_handler)

    def get_logger(self):
        """

        :return:
        """
        return self.logger

    def debug(self,message):
        """

        :param message:
        :return:
        """
        message = '='*6 + message + '='*6
        return self.logger.debug(message)

    def info(self, message):
        """

        :param message:
        :return:
        """
        message = '=' * 6 + message + '=' * 6
        return self.logger.info(message)

    def warning(self, message):
        """

        :param message:
        :return:
        """
        message = '=' * 6 + message + '=' * 6
        return self.logger.warning(message)

    def error(self, message):
        """

        :param message:
        :return:
        """
        message = '=' * 6 + message + '=' * 6
        return self.logger.error(message)

    def critical(self, message):
        """

        :param message:
        :return:
        """
        message = '=' * 6 + message + '=' * 6
        return self.logger.critical(message)




log = HandleLog()
if __name__ == '__main__':
    log = HandleLog()
    log.info('test')
    log.logger.info("test1")


