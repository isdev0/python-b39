import jsonpickle
import importlib
import json
import os.path
import pytest
from fixture.application import Application
from fixture.db import DbFixture
from fixture.orm import ORMFixture

fixture = None
config  = None


def load_config(file):
    global config
    if config is None:
        config_json = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_json) as f:
            config = json.load(f)
    return config


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--config"))["web"]
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config["base_url"])
    fixture.session.do_login(username=web_config["username"], password=web_config["password"])
    return fixture


@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--config"))['db']
    dbfixture = DbFixture(host=db_config["host"], port=db_config["port"], database=db_config["database"], user=db_config["user"], password=db_config["password"])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture


@pytest.fixture(scope="session")
def orm(request):
    db_config = load_config(request.config.getoption("--config"))['db']
    ormfixture = ORMFixture(host=db_config["host"], port=db_config["port"], database=db_config["database"], user=db_config["user"], password=db_config["password"])
    def fin():
        ormfixture.destroy()
    request.addfinalizer(fin)
    return ormfixture


@pytest.fixture(scope="session", autouse=True)
def terminate(request):
    def fin():
        fixture.session.do_logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


@pytest.fixture()
def check_ui(request):
    return request.config.getoption("--check_ui")


def pytest_addoption(parser):
    parser.addoption("--browser",  action="store", default="firefox")
    parser.addoption("--config",   action="store", default="config.json")
    parser.addoption("--check_ui", action="store_true")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())
