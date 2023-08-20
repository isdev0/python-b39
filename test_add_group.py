# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from group import Group
import unittest

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        #self.wd = webdriver.Chrome()
        self.wd.maximize_window()
        self.wd.implicitly_wait(30)

    def create_group(self, wd, group):
        # create new group
        wd.find_element(By.NAME, "new").click()

        # fill out group values
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").clear()
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").clear()
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)

        # save new group
        wd.find_element(By.NAME, "submit").click()

    def login(self, wd, username, password):
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").click()
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def open_internal_page(self, wd, tab):
        wd.find_element(By.LINK_TEXT, tab).click()

    def open_external_page(self, wd, url):
        wd.get(url)

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True



    def test_add_group(self):
        wd = self.wd
        self.open_external_page(wd, "http://localhost/addressbook/")
        self.login(wd, username="admin", password="secret")
        self.open_internal_page(wd, "groups")
        self.create_group(wd, Group(name="123123", header="123", footer="234"))
        self.open_internal_page(wd, "groups")
        self.open_internal_page(wd, "Logout")

    def test_add_empty_group(self):
        wd = self.wd
        self.open_external_page(wd, "http://localhost/addressbook/")
        self.login(wd, username="admin", password="secret")
        self.open_internal_page(wd, "groups")
        self.create_group(wd, Group(name="", header="", footer=""))
        self.open_internal_page(wd, "groups")
        self.open_internal_page(wd, "Logout")

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
