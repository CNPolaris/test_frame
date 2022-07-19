# -*- coding: utf-8 -*-
# @Time    : 2022/7/18 14:30
# @FileName: basic_api.py
# @Author  : CNPolaris
import json
import re

from utils.library import API
from utils.config import config
from data_io.data_io import TestDataIO
from utils.logger import logger


class BasicApi(API):
    """
    API接口最上层的基础类,用户封装
    """

    def __init__(self):
        super().__init__()
        self.config = config
        self.io = TestDataIO()

    @staticmethod
    def get_variable_name(json_str):
        """
        正则匹配：返回转换后、原始数据列表，排序相同：['auditId', 'auditResult',...] ['${auditId}', '${auditResult}',...]
        @param json_str: json 串
        @return:
        """
        origin_list = re.findall(r'\${.*?\}', json_str)
        cooked_list = list()
        for x in origin_list:
            a = x.replace("{", "").replace("}", "").replace("$", "")
            cooked_list.append(a)
        return cooked_list, origin_list

    def filling_missing(self, origin_body, param_info):
        """
        填充补全数据，只补全需要的值（即${}里的值），再以原始格式返回补全值后的信息
        @param origin_body: 原始请求体str型字典、或者普通str or dict() 都可以
        @param param_info:  字典集 key:value 形式，用key取到value替换返回
        @return:
        """
        if isinstance(origin_body, dict):
            origin_body = json.dumps(origin_body)
        cooked_list, origin_list = self.get_variable_name(origin_body)
        cooked_list = tuple(cooked_list)
        origin_list = tuple(origin_list)
        if isinstance(param_info, str):
            param_info = json.loads(param_info)
        for cooked_param, origin_param in zip(cooked_list, origin_list):
            origin_body = origin_body.replace(origin_param, str(param_info[cooked_param]))
        try:
            switched_body = json.loads(origin_body)
        except Exception as e:
            logger.debug(origin_body + " 无法转成字典类型！")
            return origin_body
        else:
            return switched_body

    def complete_url(self, api_data):
        """
        组装出完整的URL
        :param api_data: 从API表取到的单条接口数据：{'id': 4, 'name': '新增热门新闻', 'flag': 'API_MHSY_RMXW_add_articles', 'description': '门户首页新增新闻', 'type': 1, 'host': 'http://172.20.102.241:30000/', 'address': 'gateway/portal-api/articles/add', 'request_header': '{\r\n"Connection": "keep-alive",\r\n"Accept": "application/json, text/plain, */*",\r\n"Authorization": "",\r\n"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",\r\n"Content-Type": "application/json;charset=UTF-8",\r\n}', 'request_body': '', 'expected_response': '{\r\n    "code": 0,\r\n    "message": "成功",\r\n    "data": 3\r\n}', 'status': 1, 'created_time': datetime.datetime(2022, 6, 1, 11, 28, 15, 344837), 'update_time': datetime.datetime(2022, 6, 1, 14, 18, 17, 827862), 'module_id': 12}
        :return:
        """
        if self.config.get_api_url():
            full_url = self.config.get_api_url() + api_data["address"]
        else:
            full_url = api_data["host"] + api_data["address"]
        return full_url

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
        _api_item["params"] = self.io.get_api_params(module, file_name)
        # 获取期望
        _api_item["expect"] = self.io.get_api_validate(module, file_name)
        return _api_item

    @staticmethod
    def get_item_of_search(seq, key1, value, key2):
        """
        从查询队列中取出一条数据的主键id
        :param seq: 数据队列
        :param key1: 查询关键字
        :param value: 查询关键字的值
        :param key2: 需要取出的关键字
        :return:
        """
        for item in seq:
            if item[key1] == value:
                return item[key2]
        return None


if __name__ == '__main__':
    print(BasicApi().get_api_item("home", "get_admin_info.yml"))
