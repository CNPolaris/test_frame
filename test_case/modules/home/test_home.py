# -*- coding: utf-8 -*-
# @Time    : 2022/7/18 19:47
# @FileName: test_home.py
# @Author  : CNPolaris

import allure
import pytest

from api_src.process.home.home_process import home_process
from utils.logger import logger
from test_case.modules.basic_case import BasicCase


class TestHome(BasicCase):
    """
    首页-测试用例
    """
    @pytest.mark.all
    @pytest.mark.home
    def test_get_admin_info(self):
        logger.info("==============Case:[首页-获取登录信息]开始执行==============")
        home_process.get_home_info()
        logger.info("==============Case:[首页-获取登录信息]结束执行==============")


