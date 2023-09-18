# -*- coding: utf-8 -*-
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not(len(wd.find_elements(By.NAME, "searchstring")) > 0):
            self.app.open_internal_page("home")

    def create(self, contact):
        wd = self.app.wd

        # creating mode, default
        mode = 0

        wd.find_element(By.LINK_TEXT, "add new").click()

        self.fill_client_form(contact, mode)

        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
        self.open_home_page()

    def update_first(self, contact):
        wd = self.app.wd

        # updating mode
        mode = 1

        self.open_home_page()
        wd.find_element(By.XPATH, "//img[@alt='Edit']").click()

        self.fill_client_form(contact, mode)

        wd.find_element(By.NAME, "update").click()
        self.open_home_page()

    def delete_first(self):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element(By.NAME, "selected[]").click()
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        time.sleep(0.25) #FIXME needs to find the way to avoid delaying
        self.open_home_page()

    def fill_client_form(self, contact, mode=0):
        # mode = 0:creating
        # mode = 1:updating

        wd = self.app.wd

        self.fill_field("firstname", contact.firstname)
        self.fill_field("middlename", contact.middlename)
        self.fill_field("lastname", contact.lastname)
        self.fill_field("nickname", contact.nickname)
        self.fill_field("title", contact.title)
        self.fill_field("company", contact.company)
        self.fill_field("address", contact.address)
        self.fill_field("home", contact.home)
        self.fill_field("mobile", contact.mobile)
        self.fill_field("work", contact.work)
        self.fill_field("fax", contact.fax)
        self.fill_field("email", contact.email)
        self.fill_field("email2", contact.email2)
        self.fill_field("email3", contact.email3)
        self.fill_field("homepage", contact.homepage)
        self.fill_selector("bday", contact.bday)
        self.fill_selector("bmonth", contact.bmonth)
        self.fill_field("byear", contact.byear)
        self.fill_selector("aday", contact.aday)
        if   mode == 0: self.fill_selector("amonth", contact.amonth)
        elif mode == 1: self.fill_selector("amonth", contact.amonth.lower())
        self.fill_field("ayear", contact.ayear)
        self.fill_field("address2", contact.address2)
        self.fill_field("phone2", contact.phone2)
        self.fill_field("notes", contact.notes)

    def fill_field(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(value)

    def fill_selector(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element(By.NAME, field_name).click()
            Select(wd.find_element(By.NAME, field_name)).select_by_value(value)
            wd.find_element(By.CSS_SELECTOR, "select[name=\"" + field_name + "\"] > option[value=\"" + value + "\"]").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    def getAll(self):
        wd = self.app.wd
        self.open_home_page()

        contacts = []
        elements = wd.find_elements(By.CSS_SELECTOR, "table tr[name='entry']")
        for element in elements:
            contact = element.find_elements(By.TAG_NAME, "td")
            id          = contact[0].find_element(By.NAME, "selected[]").get_attribute("value")
            firstname   = contact[2].text
            lastname    = contact[1].text
            contacts.append(Contact(id=id, firstname=firstname, lastname=lastname))

        return contacts
