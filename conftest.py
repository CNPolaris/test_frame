# -*- coding: utf-8 -*-
# @Time    : 2022/7/18 20:33
# @FileName: conftest.py
# @Author  : CNPolaris

import os
from typing import Any, Callable, Optional

import pytest
from _pytest.fixtures import fixture, SubRequest

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


@fixture(scope="session", autouse=True)
def add_allure_environment_property(request: SubRequest) -> Optional[Callable]:
    environment_properties = dict()

    def maker(key: str, value: Any):
        environment_properties.update({key: value})

    yield maker
    alluredir = request.config.getoption(ALLUREDIR_OPTION)
    if not alluredir or not os.path.isdir(alluredir) or not environment_properties:
        return
    allure_env_path = os.path.join(alluredir, ALLURE_ENVIRONMENT_PROPERTIES_FILE)
    print(alluredir)
    print(allure_env_path)
    with open(allure_env_path, 'w') as _f:
        data = '\n'.join([f'{variable}={value}' for variable, value in environment_properties.items()])
        _f.write(data)


@fixture(autouse=True)
def cenpprop(add_allure_environment_property: Callable, get_env, request) -> None:
    add_allure_environment_property("mark", request.config.getoption("-m"))
    add_allure_environment_property("env", get_env)


def pytest_sessionstart(session):
    session.results = dict()
    mark = session.config.getoption("-m")
    os.environ['mark'] = mark


case_result = []


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # 获取钩子方法的调用结果
    out = yield
    # 从钩子方法的调用结果中获取测试报告
    report = out.get_result()
    case_dic = {}

    if report.when == 'call':
        case_dic["id"] = report.nodeid
        case_dic["outcome"] = report.outcome
        case_result.append(case_dic)
