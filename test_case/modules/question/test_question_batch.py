# -*- coding: utf-8 -*-
# @Time    : 2022/7/19 19:52
# @FileName: test_question_batch.py
# @Author  : CNPolaris
import allure
import pytest

from api_src.process.question.question_batch_process import question_batch_process as qbp
from utils.logger import logger
from test_case.modules.basic_case import BasicCase

question_list = [
    ("测试01", "A", 3, 1, None, [{'content': '测试', 'prefix': 'A'}, {'content': '测试', 'prefix': 'B'}, {'content': '擦拭', 'prefix': 'C'}, {'content': '测试', 'prefix': 'D'}],1,3,1,"测试01"),
    ("测试02", "A", 3, 1, None, [{'content': '测试', 'prefix': 'A'}, {'content': '测试', 'prefix': 'B'}, {'content': '擦拭', 'prefix': 'C'},{'content': '测试', 'prefix': 'D'}], 1, 3, 1, "测试02"),
    ("测试03", "A", 3, 1, None,[{'content': '测试', 'prefix': 'A'}, {'content': '测试', 'prefix': 'B'}, {'content': '擦拭', 'prefix': 'C'},{'content': '测试', 'prefix': 'D'}], 1, 3, 1, "测试03"),
    ("测试04", "A", 3, 1, None,[{'content': '测试', 'prefix': 'A'}, {'content': '测试', 'prefix': 'B'}, {'content': '擦拭', 'prefix': 'C'},{'content': '测试', 'prefix': 'D'}], 1, 3, 1, "测试04")
]


class TestQuestionBatch(BasicCase):

    @allure.feature("题库管理")
    @allure.story("题目-增查删改")
    @pytest.mark.all
    @pytest.mark.question
    @pytest.mark.parametrize("analyze,correct,difficult,gradeLevel,id,items,questionType,score,subjectId,title", question_list)
    def test_question_batch_add(self,analyze,correct,difficult,gradeLevel,id,items,questionType,score,subjectId,title):
        qbp.question_batch_add(analyze,correct,difficult,gradeLevel,id,items,questionType,score,subjectId,title)