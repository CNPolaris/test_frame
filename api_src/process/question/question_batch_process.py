# -*- coding: utf-8 -*-
# @Time    : 2022/7/19 19:19
# @FileName: question_batch_process.py
# @Author  : CNPolaris

from api_src.apis.question.question_batch_apis import QuestionBatchApis


class QuestionBatchProcess(object):

    def __init__(self):
        self.question = QuestionBatchApis()

    def question_batch_add(self,body):
        self.question.question_batch_add(body)


question_batch_process = QuestionBatchProcess()