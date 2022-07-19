# -*- coding: utf-8 -*-
# @Time    : 2022/7/18 14:30
# @FileName: basic_api.py
# @Author  : CNPolaris

from utils.library import API
from utils.config import config
from data_io.data_io import TestDataIO


class BasicApi(API):
    """
    API接口最上层的基础类,用户封装
    """

    def __init__(self):
        super().__init__()
        self.config = config
        self.io = TestDataIO()

    def get_api_item(self, module, file_name):
        """
        根据module模块、file_name文件名解析yml
        :param module: 模块相对路径
        :param file_name: 文件名
        :return: dict{}
        """
        _api_item = dict()
        # 获取请求类型
        _api_item["method"] = self.io.get_api_method(module, file_name)
        # 获取接口路径
        _api_item["path"] = self.io.get_api_path(module, file_name)
        # 获取请求头
        _api_item["headers"] = self.io.get_api_headers(module, file_name)
        # 获取请求体
        _api_item["body"] = self.io.get_api_body(module, file_name)
        # # 获取请求参数
        # _api_item["params"] = self.io.get_api_params(module, file_name)
        # 获取期望
        _api_item["expect"] = self.io.get_api_validate(module, file_name)
        return _api_item


if __name__ == '__main__':
    print(BasicApi().get_api_item("home", "get_admin_info.yml"))
