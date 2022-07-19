# -*- coding: utf-8 -*-
# @Time    : 2022/7/19 19:19
# @FileName: question_batch_process.py
# @Author  : CNPolaris

from api_src.apis.question.question_batch_apis import QuestionBatchApis


class QuestionBatchProcess(object):

    def __init__(self):
        self.question = QuestionBatchApis()

    def question_batch_add(self,analyze,correct,difficult,gradeLevel,id,items,questionType,score,subjectId,title):
        self.question.question_batch_add(analyze,correct,difficult,gradeLevel,id,items,questionType,score,subjectId,title)


question_batch_process = QuestionBatchProcess()