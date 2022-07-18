# -*- coding: utf-8 -*-
# @Time    : 2022/7/18 19:41
# @FileName: home_process.py
# @Author  : CNPolaris
# 首页相关的业务流程

from api_src.apis.home.home_apis import HomeApis
from utils.logger import logger


class HomeProcess(object):
    """
    首页-接口串联场景
    """

    def __init__(self):
        self.home = HomeApis()

    def get_home_info(self):
        """
        获取首页的信息
        :return:
        """
        logger.info("================首页-获取首页信息================")
        self.home.admin_info()


home_process = HomeProcess()