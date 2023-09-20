import importlib
import json
import os.path
import pytest
from fixture.application import Application

fixture = None
config  = None


@pytest.fixture
def app(request):
    global fixture
    global config

    browser = request.config.getoption("--browser")

    if config is None:
        config_json = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--config"))
        with open(config_json) as f:
            config = json.load(f)

    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=config["base_url"])

    fixture.session.do_login(username=config["username"], password=config["password"])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def terminate(request):
    def fin():
        fixture.session.do_logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser",  action="store", default="firefox")
    parser.addoption("--config", action="store", default="config.json")

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata
