# -*- coding: utf-8 -*-
# @Time    : 2022/7/19 17:29
# @FileName: question_batch_apis.py
# @Author  : CNPolaris

import os

from api_src.apis.basic_api import BasicApi
from utils.config import config
from utils.library import api
from utils.login_service import login
from utils.api_global import api_global as ag


class QuestionBatchApis(BasicApi):

    def __init__(self):
        super().__init__()
        self.login = login
        self.file_name = os.path.dirname(os.path.realpath(__file__)).split(os.sep)[-1]
        self.module_path = self.file_name.replace("/", os.sep)

    def question_batch_add(self, body):
        # 公有0--解析接口有关数据 0.method 1.path 2.headers 3.body 4.expect
        api_item = self.get_api_item(self.module_path, "question_add.yml")
        # 公有--替换数据
        api_item["body"] = body
        # 公有1--拼接完整的url请求路径 base_url(根据环境env) + yml中接口路径
        api_item["path"] = config.get_base_url() + api_item["path"]
        # 公有2--组装请求标头headers 形成携带token的headers yml中headers + 用最新拿到的token替换Authorization - values
        api_item["headers"]["Authorization"] = self.login.get_admin_token()
        # 公有3--主接口发起请求：获取首页数据信息
        _response = api.request(api_item["method"], api_item["path"], api_item["headers"], api_item["body"],
                                api_item["params"],
                                api_item["expect"])
        # 公有4--断言判断接口是否真正请求成功
        assert _response.json()["code"] == api_item["expect"]["code"]
        return _response.json()

    def question_batch_search(self, title):
        # 公有0--解析接口有关数据 0.method 1.path 2.headers 3.body 4.expect
        api_item = self.get_api_item(self.module_path, "question_search.yml")
        # 公有1--拼接完整的url请求路径 base_url(根据环境env) + yml中接口路径
        api_item["path"] = config.get_base_url() + api_item["path"]
        # 公有2--组装请求标头headers 形成携带token的headers yml中headers + 用最新拿到的token替换Authorization - values
        api_item["headers"]["Authorization"] = self.login.get_admin_token()
        # 公有3--主接口发起请求：获取首页数据信息
        _response = api.request(api_item["method"], api_item["path"], api_item["headers"], api_item["body"],
                                api_item["params"],
                                api_item["expect"])
        ag.api_param["question_id"] = self.get_item_of_search(_response.json()["data"]["data"], "shortTitle",title, "id")
        # 公有4--断言判断接口是否真正请求成功
        assert _response.json()["code"] == api_item["expect"]["code"]
        return _response.json()

    def question_batch_delete(self):
        # 公有0--解析接口有关数据 0.method 1.path 2.headers 3.body 4.expect
        api_item = self.get_api_item(self.module_path, "question_delete.yml")
        # 公有1--拼接完整的url请求路径 base_url(根据环境env) + yml中接口路径
        api_item["path"] = config.get_base_url() + self.filling_missing(api_item["path"], ag.api_param)
        # 公有2--组装请求标头headers 形成携带token的headers yml中headers + 用最新拿到的token替换Authorization - values
        api_item["headers"]["Authorization"] = self.login.get_admin_token()
        # 私有--补全path
        # 公有3--主接口发起请求：获取首页数据信息
        _response = api.request(api_item["method"], api_item["path"], api_item["headers"], api_item["body"],
                                api_item["params"],
                                api_item["expect"])
        # 公有4--断言判断接口是否真正请求成功
        assert _response.json()["code"] == api_item["expect"]["code"]
        return _response.json()

# if __name__ == '__main__':
    # os.environ['env'] = "admin"
    # QuestionBatchApis().question_batch_add()