import BSTestRunner
import os, sys, unittest, time
base_path = os.path.dirname(os.getcwd())
sys.path.append(base_path)

class RunCase():

    """执行测试用例，生成测试报告"""

    def get_case_suite(self):
        """获取测试集"""
        start_dir = os.path.join(base_path,"case")
        discover = unittest.defaultTestLoader.discover(start_dir,pattern="test*.py")
        return discover

    def write_report(self):
        """写入测试报告"""

        nowtime = time.strftime("%Y-%m-%d %H-%M-%S")
        filename = os.path.join(base_path, "report", "{}report.html".format(nowtime))
        with open(filename,"wb") as f:
            runner = BSTestRunner.BSTestRunner(stream=f, title="自动化测试报告", description="自动化测试报告",verbosity=2)
            runner.run(self.get_case_suite())


run = RunCase()
if __name__ == '__main__':
    run.write_report()

