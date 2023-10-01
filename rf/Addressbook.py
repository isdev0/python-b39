import json
import os.path
from fixture.application import Application
from fixture.db import DbFixture
from model.group import Group


class Addressbook:
    ROBOT_LIBRARY_SCOPE = "SUITE"

    def __init__(self, config="config.json", browser="chrome"):
        self.browser = browser

        config_json = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", config)
        with open(config_json) as f: self.config = json.load(f)

    def init_fixtures(self):
        web_config = self.config["web"]
        self.fixture = Application(browser=self.browser, base_url=web_config["base_url"])

        self.fixture.session.do_login(username=web_config["username"], password=web_config["password"])

        db_config = self.config['db']
        self.dbfixture = DbFixture(host=db_config["host"], port=db_config["port"], database=db_config["database"], user=db_config["user"], password=db_config["password"])

    def destroy_fixtures(self):
        self.dbfixture.destroy()
        self.fixture.destroy()

    def create_group(self, name, header, footer):
        self.fixture.group.create(Group(name=name, header=header, footer=footer))
