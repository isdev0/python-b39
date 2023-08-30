# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        #self.wd = webdriver.Chrome()
        self.wd.maximize_window()
        self.wd.implicitly_wait(30)
        self.session    = SessionHelper(self)
        self.group      = GroupHelper(self)
        self.contact    = ContactHelper(self)

    def open_internal_page(self, tab):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, tab).click()

    def open_external_page(self, url):
        wd = self.wd
        wd.get(url)

    def destroy(self):
        self.wd.quit()
