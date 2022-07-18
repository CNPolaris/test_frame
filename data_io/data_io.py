# -*- coding: utf-8 -*-
# @Time    : 2022/7/18 14:33
# @FileName: data_io.py
# @Author  : CNPolaris

import operator as op
import os

import yaml

from utils.config import config


class TestDataIO(object):
    """
    接口自动化相关数据读取&输出
    """

    def __init__(self):
        pass

    @staticmethod
    def read_yaml(module, file_name):
        """
        @param module: 模块相对路径，例：mhsy/rmxw,写法："mhsy{}rmxw".format(os.sep)
        @param file_name: 文件名：articles_add.yml or articles_add均可
        @return: dict()形式输出
        """
        if op.contains(file_name, ".yml"):
            full_path = config.get_test_data_path() + "{}{}{}".format(module, os.sep, file_name)
        else:
            full_path = config.get_test_data_path() + "{}{}{}.yml".format(module, os.sep, file_name)
        with open(full_path, 'r', encoding="utf-8") as f:
            _yaml = yaml.safe_load(f.read())
        return _yaml

    def get_api_method(self, module, file_name):
        """
        抓取yml里api请求类型：post get put
        @param module: 模块相对路径，例：mhsy/rmxw,写法："mhsy{}rmxw".format(os.sep)
        @param file_name: 文件名：articles_add.yml or articles_add均可
        @return: 格式样例：POST
        """
        return self.read_yaml(module, file_name)["teststeps"][0]["request"]["method"]

    def get_api_path(self, module, file_name):
        """
        抓取yml里api路径：/gateway/portal-api/articles/operate
        @param module: 模块相对路径，例：mhsy/rmxw,写法："mhsy{}rmxw".format(os.sep)
        @param file_name: 文件名：articles_add.yml or articles_add均可
        @return: 格式样例：POST
        """
        return self.read_yaml(module, file_name)["teststeps"][0]["name"]

    def get_api_headers(self, module, file_name):
        """
        抓取yml里请求头
        @param module: 模块相对路径，例：mhsy/rmxw,写法："mhsy{}rmxw".format(os.sep)
        @param file_name: 文件名：articles_add.yml or articles_add均可
        @return:格式样例：{'Authorization': 'Bearer ...', 'Content-Type': 'application/json;charset=UTF-8', 'User-Agent': 'Mozilla/5.0 ...'}
        """
        return self.read_yaml(module, file_name)["teststeps"][0]["request"]["headers"]

    def get_api_body(self, module, file_name):
        """
        抓取yml里请求体
        @param module: 模块相对路径，例：mhsy/rmxw,写法："mhsy{}rmxw".format(os.sep)
        @param file_name: 文件名：articles_add.yml or articles_add均可
        @return:格式样例：{'content': '<p>为了迎接..</p>', 'desc': '特别..', 'image': 'http..', 'title': '自动化..'}
        """
        try:
            self.read_yaml(module, file_name)["teststeps"][0]["request"]["json"]
        except Exception as e:
            return None
        else:
            return self.read_yaml(module, file_name)["teststeps"][0]["request"]["json"]

    def get_api_params(self, module, file_name):
        """
        抓取yml里请求参数
        :param module: 模块相对路径
        :param file_name: 文件名
        :return:
        """
        try:
            self.read_yaml(module, file_name)["teststeps"][0]["request"]["params"]
        except Exception as e:
            return None
        else:
            return self.read_yaml(module,file_name)["teststeps"][0]["request"]["params"]

    def get_api_validate(self, module, file_name):
        """
        抓取yml里响应体（剔除headers）,作为预期值用来断言请求是否正常
        @param module: 模块相对路径，例：mhsy/rmxw,写法："mhsy{}rmxw".format(os.sep)
        @param file_name: 文件名：articles_add.yml or articles_add均可
        @return: 格式样例：{'status_code': 200, 'code': 0, 'message': '成功', 'data': 94}
        """
        y_data = self.read_yaml(module, file_name)["teststeps"][0]["validate"]
        api_info = dict()
        for _data in y_data:
            for _key, _value in _data.items():
                if op.ne(_value[0].split(".")[0], "headers"):
                    api_info[_value[0].split(".")[-1]] = _value[1]
        return api_info


if __name__ == "__main__":
    print(TestDataIO().get_api_validate("home", "get_admin_info.yml"))
