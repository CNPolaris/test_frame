# -*- coding: utf-8 -*-
# @Time    : 2022/7/18 11:20
# @FileName: logger.py
# @Author  : CNPolaris
# 日志配置

import logging

from utils.config import config

log_index = config.get_config_data('log_level').upper()
log_level = {'DEBUG': logging.DEBUG, 'INFO': logging.INFO,
             'WARN': logging.WARN, 'ERROR': logging.ERROR,
             'CRITICAL': logging.CRITICAL}

# 1、创建一个logger
logger = logging.getLogger()
logger.setLevel(log_level[log_index])  # Log等级总开关
# 2、创建一个handler,用于写入日志文件
fh = logging.FileHandler(config.get_log_path(), mode='a')  # open日志文件 方式：w a
fh.setLevel(log_level[log_index])
# 3、再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()  # open日志文件
ch.setLevel(log_level[log_index])
# 4、定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[line:%(lineno)d]: %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# 5、将两个句柄添加到handler里
logger.addHandler(fh)
logger.addHandler(ch)
# # 6、输出日志
# logger.debug("infomation")
logger.info("infomation")