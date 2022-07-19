# -*- coding: utf-8 -*-
# @Time    : 2022/7/19 16:34
# @FileName: api_global.py
# @Author  : CNPolaris


class ApiGlobal(object):

    def __init__(self):
        super().__init__()
        self.__headers = dict()  # 接口请求头
        self.__api_param = dict()  # 接口自动化流转参数

    @property
    def api_param(self):
        """
        接口自动化流转参数，释义：
        api自动化运行过程中，各个接口间流转用到的参数，例如：a接口新增某记录，记录ID为1,b接口需要审核这个id关联的记录。这个ID就是中间参数
        :param api_param = {
            "article_id":1 新增的文章id
            "XXXX":xx
        }
        :return:
        """
        return self.__api_param

    @api_param.setter
    def api_param(self, api_param):
        self.__api_param = api_param

    @property
    def headers(self):
        """
        用例运行明细, 包含：
        :param headers = {
            "admin":{
                "Accept":*/*
                "Authorization":"Bearer XX_token"}
            "admin_x":{
                "Accept":*/*
                "Authorization":"Bearer XX_token"}
            "yewu":{
                "Accept":*/*
                "Authorization":"Bearer XX_token"}
            "kaifa":{
                "Accept":*/*
                "Authorization":"Bearer XX_token"}
        }
        :return:
        """
        return self.__headers

    @headers.setter
    def headers(self, headers):
        self.__headers = headers


api_global = ApiGlobal()
