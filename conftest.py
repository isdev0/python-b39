import json
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
        with open(request.config.getoption("--config")) as config_json:
            config = json.load(config_json)

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
