# -*- coding: utf-8 -*-
# @Time    : 2022/7/18 20:10
# @FileName: run_test.py
# @Author  : CNPolaris

import os
import pytest

from utils.config import config

os.environ["isc"] = "False"
os.environ["env"] = "admin"

if __name__ == '__main__':
    result_path, report_path = config.allure_report_path()
    test_case = config.get_test_case_path()
    # pytest.main(["-vs", test_case, "-m home", "--env=admin", "--isc=False", "--is_vc=True",
    #              "--email=False",
    #              "-sq", "--alluredir", result_path])
    pytest.main()