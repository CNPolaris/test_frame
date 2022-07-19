# -*- coding: utf-8 -*-
# @Time    : 2022/7/19 19:19
# @FileName: question_batch_process.py
# @Author  : CNPolaris

from api_src.apis.question.question_batch_apis import QuestionBatchApis
from utils.logger import logger


class QuestionBatchProcess(object):

    def __init__(self):
        self.question = QuestionBatchApis()

    def question_batch_add_search_delete(self,body, title):
        logger.info("===============题库-批量测试-添加===============")
        self.question.question_batch_add(body)
        logger.info("===============题库-批量测试-查询===============")
        self.question.question_batch_search(title)
        logger.info("===============题库-批量测试-删除===============")
        self.question.question_batch_delete()


question_batch_process = QuestionBatchProcess()