# -*- coding: utf-8 -*-
# @Time    : 2022/7/18 10:05
# @FileName: config.py
# @Author  : CNPolaris

import os
import operator
import datetime
from configparser import RawConfigParser

# 项目的绝对路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


class Config(object):
    """
    读取配置文件
    """

    def __init__(self):
        # 项目地址
        self.project_path = BASE_DIR + os.sep
        # 配置文件路径
        self._config_path = self.project_path + 'setup.cfg'
        # 读取配置文件的全部信息
        self.config_parser = RawConfigParser()
        self.config_parser.read(self._config_path, 'utf-8')

    def get_config_data(self, option='', section='common_info'):
        """
        获取配置文件中的某项信息
        :param option: 参数名
        :param section: 橙色标题名
        :return: 按条件返回某条 setup.cfg值
        """
        return self.config_parser.get(section, option)

    def get_log_path(self):
        """
        文件存在则返回，否则新建后返回
        :return: 文件路径：日期.log
        """
        log_path = self.project_path + "data_io{}logs{}".format(os.sep, os.sep)
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        return log_path + "{}.log".format(str(datetime.date.today()))

    def get_test_data_path(self):
        """
        读取test_data路径
        """
        return self.project_path + "test_data{}".format(os.sep, os.sep)

    def get_test_case_path(self):
        """
        读取接口自动化测试test_case路径
        """
        return self.project_path + "test_case{}modules".format(os.sep, os.sep)

    def report_path(self):
        """
        获取测试报告的路径，文件存在则返回，否则新建后返回
        """
        report_path = self.project_path + "data_io{}allure{}".format(os.sep, os.sep)
        if not os.path.exists(report_path):
            os.makedirs(report_path)
        return report_path

    def file_store(self):
        """
        文件存在则返回，否则新建后返回
        :return: 文件路径：日期.log
        """
        report_path = self.project_path + "data_io{}test_files{}back{}".format(os.sep, os.sep, os.sep)
        if not os.path.exists(report_path):
            os.makedirs(report_path)
        return report_path

    def allure_report_path(self):
        """
        文件存在则返回，否则新建后返回
        :return: 文件路径：日期.log
        """
        report_path = self.report_path() + "report{}".format(os.sep)
        result_path = self.report_path() + "result{}".format(os.sep)
        if not os.path.exists(report_path):
            os.makedirs(report_path)
        if not os.path.exists(result_path):
            os.makedirs(result_path)
        return result_path, report_path

    @staticmethod
    def get_base_url():
        """
        根据指定的env读取setup.cfg的环境配置中的host（主机地址）作为全局接口的base_url，此时返回url
        """
        base_url = config.get_config_data("base_url", section=os.environ.get("env"))
        if operator.eq(base_url[-1], "/"):
            base_url = base_url[:-1]
        return base_url

    @staticmethod
    def get_login_in_url():
        """
        读取配置文件中的login_in_url
        :return: /admin/login
        """
        return config.get_config_data("login_in_url", section=os.environ.get("env"))

    @staticmethod
    def get_admin():
        """
        读取配置文件中的管理员账号、密码
        :return:{'username': 'admin', 'password': '123456'}
        """
        user_info = {}
        # 读取环境
        env = os.environ.get("env")
        user_info["username"] = config.get_config_data("admin_username", env)
        user_info["password"] = config.get_config_data("admin_password", env)
        return user_info


config = Config()

# if __name__ == '__main__':
#     os.environ['env'] = 'admin'
#     config = Config()
#     print(config.get_test_case_path())
