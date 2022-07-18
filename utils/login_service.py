# -*- coding: utf-8 -*-
# @Time    : 2022/7/18 10:03
# @FileName: login_service.py
# @Author  : CNPolaris
# desc 登录服务

import os
import operator
import requests

from utils.config import config
from utils.logger import logger


class LoginService(object):
    """
    登录服务用于提供最新的token
    """

    def __init__(self):
        self.config = config

    def get_admin_token(self):
        """
        获取管理员token
        :return:
        """
        return self.get_token(self.config.get_admin(), self.config.get_base_url())

    @staticmethod
    def login_in(user_info, base_url):
        """
        登录网站，并获取响应结果
        :param user_info: 用户信息：{'username': 'student','password': '123456'}
        :param base_url: 前置url： https://admin-api.macrozheng.com/
        :return: response: 响应结果：{"code":200,"message":"操作成功","data":{"tokenHead":"Bearer ","token":"eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbiIsImNyZWF0ZWQiOjE2NTgxMTUzMzM4NzcsImV4cCI6MTY1ODcyMDEzM30.0wI8NwCWNifnKWZ1p_qAZ69-Ct4HSGJ9K-6aG4BuyD-05DwFxm9K6XXBQOg2I_zRhoRsS3e5aHOYCb-TpWz2Yw"}}
        """
        # 拼接完整的登录url
        login_in_url = base_url + config.get_login_in_url()
        response = requests.post(url=login_in_url, json=user_info, stream=True)
        return response

    def get_token(self, user_info, base_url):
        """
        从登录的响应结果中读取token
        :param user_info:
        :param base_url:
        :return:
        """
        try:
            if operator.ne(base_url[-1], "/"):
                base_url = base_url
            _response = self.login_in(user_info, base_url)
            _token = "Bearer " + _response.json()['data']['token']
            return _token
        except Exception as e:
            return None


login = LoginService()
