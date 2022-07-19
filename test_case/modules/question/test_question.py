# -*- coding: utf-8 -*-
# @Time    : 2022/7/19 17:04
# @FileName: test_question.py
# @Author  : CNPolaris

import allure
import pytest

from api_src.process.question.question_process import question_process
from utils.logger import logger
from test_case.modules.basic_case import BasicCase


class TestQuestion(BasicCase):
    @allure.feature("题库管理")
    @allure.story("题目-增查删改")
    @pytest.mark.all
    @pytest.mark.question
    def test_question_add_search_update_delete(self):
        logger.info("==============Case:[题目-增查删改]开始执行==============")
        question_process.question_add_search_update_delete()
        logger.info("==============Case:[题目-增查删改]结束执行==============")
