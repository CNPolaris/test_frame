# -*- coding: utf-8 -*-
# @Time    : 2022/7/18 13:21
# @FileName: library.py
# @Author  : CNPolaris
# 常用工具的自写封装库


import json
import os
import requests
import xlrd

from utils.logger import logger


class Excel(object):
    """
    Excel工具类简易封装
    """
    @staticmethod
    def read_excel(excel_path, sheet_num=0):
        """
        读取excel文件，返回一个sheet对象
        :param excel_path: 文件的绝对路径 需要类型：str
        :param sheet_num: sheet编号 默认值0
        :return:
        """
        try:
            workbook = xlrd.open_workbook(excel_path)
            book_sheet = workbook.sheet_by_index(sheet_num)
        except Exception as e:
            return e
        else:
            return book_sheet

    @staticmethod
    def read_excel_to_list(excel_path, sheet_num=0):
        """
        读取excel数据转换成list[dict{}]
        :param excel_path: 文件的绝对路径 需要类型：str excel文件格式xls
        :param sheet_num: table index
        :return:  返回表头、和读取结果
        """
        # 读取excel
        table = excel.read_excel(excel_path, sheet_num)
        # 保存读取结果
        result = []
        # 表头
        table_params = table.row_values(0)
        # 按行读取
        for r in range(1, table.nrows):
            # 临时变量 {}
            temp = {}
            # 按列读取数据
            for l in range(table.ncols):
                temp[table_params[l]] = table.row_values(r)[l]
            result.append(temp)
        return table_params, result


class API(object):
    """
    对requests.request进行封装，以提供方便的测试使用
    """

    def __init__(self):
        pass

    @staticmethod
    def request(method, url, headers, request_json, request_query, expect_dict):
        """
        request 接口测试，请求结束后含请求头，请求体
        :param method: 接口的请求类型 get post put delete
        :param url: 完整的接口url 需要类型：str
        :param headers: 请求头 需要类型：dict()
        :param request_json: 请求体 需要类型：json，str
        :param request_query: 请求参数 需要类型：dict(), list[]
        :param expect_dict: 期望结果 需要类型：dict()
        :return: response 响应结果
        """
        response = requests.request(method=method, url=url, headers=headers, json=request_json, params= request_query,
                                    verify=False)
        tips_code = "{}接口：{} 响应异常！预期:{} 实际:{}".format(method, url, expect_dict["status_code"], response.status_code)
        # 断言判断请求是否成功
        assert expect_dict["status_code"] == response.status_code, tips_code
        """
        http状态码以及说明
        1xx:请求已经被接受，需要继续处理
        2xx:代表请求已经成功被服务器接收、理解、并接受
        3xx:代表页面需要重定向
        4xx:代表客户端错误，如页面没找到，或格式错误
        5xx:代表服务器错误，如找不到服务器
        """
        if response.status_code == 200:
            # 请求成功
            logger.info("=============================================")
            logger.info("====={}接口：{} 请求成功！=====".format(method, url))
            logger.info("Request headers:{}".format(headers))
            logger.info("Request Body:{}".format(request_json))
            logger.info("Request Params:{}".format(request_query))
            logger.info("Status Code:{}".format(response.status_code))
            logger.info("Response Body:{}".format(response.text))
            return response


api = API()
excel = Excel()

# if __name__ == '__main__':

