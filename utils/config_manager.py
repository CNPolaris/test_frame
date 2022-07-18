# -*- coding: utf-8 -*-
# @Time    : 2022/7/18 20:38
# @FileName: config_manager.py
# @Author  : CNPolaris
import configparser
import os

MODULE_NAME = os.path.abspath(os.path.dirname(__file__)).split('utils')[0]


def get_root_path():
    cur_path = os.path.abspath(os.path.dirname(__file__))
    root_path = cur_path[:cur_path.rfind(MODULE_NAME) + len(MODULE_NAME)]
    return root_path


def get_config():
    root_path = get_root_path()
    config = configparser.ConfigParser()
    config.read(root_path + '%ssetup.cfg' % os.sep, encoding='utf-8')
    return config


if __name__ == '__main__':
    # print(os.path.abspath(os.path.dirname(__file__)).split('shippingSchedule')[0])
    # print(os.path.abspath(os.path.dirname(__file__)).split('utils')[0])
    print(get_root_path())
