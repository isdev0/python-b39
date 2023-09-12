# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd

        self.app.open_internal_page("groups")
        wd.find_element(By.NAME, "new").click()

        self.fill_group_form(group)

        wd.find_element(By.NAME, "submit").click()
        self.app.open_internal_page("groups")

    def update_first(self, group):
        wd = self.app.wd

        self.app.open_internal_page("groups")
        wd.find_element(By.NAME, "selected[]").click()
        wd.find_element(By.NAME, "edit").click()

        self.fill_group_form(group)

        wd.find_element(By.NAME, "update").click()
        self.app.open_internal_page("groups")

    def delete_first(self):
        wd = self.app.wd
        self.app.open_internal_page("groups")
        wd.find_element(By.NAME, "selected[]").click()
        wd.find_element(By.NAME, "delete").click()
        self.app.open_internal_page("groups")

    def fill_group_form(self, group):
        self.fill_field("group_name", group.name)
        self.fill_field("group_header", group.header)
        self.fill_field("group_footer", group.footer)

    def fill_field(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(value)

    def count(self):
        wd = self.app.wd
        self.app.open_internal_page("groups")
        return len(wd.find_elements(By.NAME, "selected[]"))
