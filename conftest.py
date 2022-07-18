# -*- coding: utf-8 -*-
# @Time    : 2022/7/18 20:33
# @FileName: conftest.py
# @Author  : CNPolaris
import ast
import json
import os
from datetime import datetime

import pytest
import requests
from _pytest.fixtures import fixture

from utils.config_manager import get_config, get_root_path

ALLURE_ENVIRONMENT_PROPERTIES_FILE = "environment.properties"
ALLUREDIR_OPTION = "--alluredir"

cfg = get_config()


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="admin", help="Test environment: test for default.")
    parser.addoption("--isc", action="store", default="False", help="if login with isc account")
    parser.addoption("--is_vc", action="store", default="False", help="if relating vc")
    parser.addoption("--site_code", action="store", default="GWZB", help="set your site code")
    parser.addoption("--email", action="store", default="False", help="if sendmail")


@pytest.fixture(scope="session", autouse=True)
def get_env(request):
    print(get_root_path())
    env = request.config.getoption("--env")
    os.environ['env'] = env
    return env


@pytest.fixture(scope="session", autouse=True)
def is_isc(request):
    isc = request.config.getoption("--isc")
    os.environ['isc'] = isc
    return isc


@fixture(scope="session", autouse=True)
def set_base_url(get_env):
    base_url = cfg.get(get_env, 'base_url')
    print(base_url)
    return base_url


@pytest.fixture(scope="session", autouse=True)
def site_code(request):
    site_code = request.config.getoption("--site_code")
    os.environ['site_code'] = site_code
    return site_code


@pytest.fixture(scope="session", autouse=True)
def ifRelatingVc(request):
    is_vc = request.config.getoption("--is_vc")
    os.environ['is_vc'] = is_vc
    return is_vc


@fixture(scope="session", autouse=True)
def set_base_url(get_env):
    base_url = cfg.get(get_env, 'base_url')
    print(base_url)
    return base_url


@fixture(scope="session", autouse=True)
def set_user_header(get_env):
    username = get_config().get(get_env, 'username')
    userid = get_config().get(get_env, 'userid')
    header = {'x-user-id': userid, 'x-user-login': username}
    return header
