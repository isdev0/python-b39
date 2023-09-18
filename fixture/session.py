# -*- coding: utf-8 -*-
import time

from selenium.webdriver.common.by import By

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_external_page("http://localhost/addressbook/")
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").click()
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        self.app.open_internal_page("Logout")
        wd.find_element(By.NAME, "user")
        #time.sleep(0.25)

    def is_login(self):
        wd = self.app.wd
        return len(wd.find_elements(By.LINK_TEXT, "Logout")) > 0

    def is_login_as(self, username):
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//div/div[1]/form/b").text[1:-1]

    def do_login(self, username, password):
        wd = self.app.wd
        if self.is_login():
            if self.is_login_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def do_logout(self):
        wd = self.app.wd
        if len(wd.find_elements(By.LINK_TEXT, "Logout")) > 0:
            self.logout()
