# -*- coding: utf-8 -*-
# @Time    : 2022/7/18 19:54
# @FileName: basic_case.py
# @Author  : CNPolaris

import os
from datetime import datetime

from utils.logger import logger


class BasicCase(object):
    """
    测试用例基类
    """

    def setup_class(self):
        self.start_time = datetime.now()
        logger.info("===============用例于{}开始执行===============".format(self.start_time))

    def teardown_class(self):
        self.end_time = datetime.now()
        self.duration_time = self.end_time - self.start_time
        logger.info("===============用例于{}全部执行结束,总用时：{}===============".format(self.end_time, self.duration_time))
