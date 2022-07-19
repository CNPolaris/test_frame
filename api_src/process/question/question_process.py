# -*- coding: utf-8 -*-
# @Time    : 2022/7/19 16:41
# @FileName: question_process.py
# @Author  : CNPolaris

from api_src.apis.question.question_apis import QuestionApi
from utils.logger import logger


class QuestionProcess(object):
    """
    题目接口串联
    """

    def __init__(self):
        self.question = QuestionApi()

    def question_add_search_update_delete(self):
        """
        题目增删改查串联测试
        :return:
        """
        logger.info("===============题库-增查改删===============")
        self.question.question_add()
        self.question.question_search()
        self.question.question_delete()


question_process = QuestionProcess()
