import BSTestRunner
import os, sys, unittest, time
base_path = os.path.dirname(__file__)
# print(base_path)
sys.path.append(base_path)


"""执行测试用例，生成测试报告"""
start_dir = os.path.join(base_path, "case")
# start_dir = base_path + "/case"
# print(start_dir)
discover = unittest.defaultTestLoader.discover(start_dir, pattern="test_*_*.py")
nowtime = time.strftime("%Y-%m-%d %H_%M_%S")
# print(nowtime)
report_name = os.path.join(base_path, "report", "{}.html".format(nowtime))
# report_name = base_path + "/report/" + "{}.html".format(nowtime)
print(report_name)
with open(report_name, 'wb') as f:
    runner = BSTestRunner.BSTestRunner(stream=f, title="{}自动化测试报告", description="测试报告", verbosity=2)
    runner.run(discover)




