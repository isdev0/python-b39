# -*- coding: utf-8 -*-
import time, re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from model.contact import Contact


class ContactHelper:
    contact_cache = None

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not(len(wd.find_elements(By.NAME, "searchstring")) > 0):
            self.app.open_internal_page("home")

    def open_contact_by_index(self, index, title="Edit"):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements(By.XPATH, "//img[@title='" + title + "']")[index].click()

    def open_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element(By.CSS_SELECTOR, "a[href='edit.php?id=" + id + "']").click()

    def create(self, contact):
        wd = self.app.wd

        # creating mode, default
        mode = 0

        wd.find_element(By.LINK_TEXT, "add new").click()

        self.fill_client_form(contact, mode)

        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
        self.open_home_page()
        self.contact_cache = None

    def update_first(self, contact):
        self.update_by_index(0)

    def update_by_index(self, index, contact):
        wd = self.app.wd

        # updating mode
        mode = 1

        self.open_contact_by_index(index, "Edit")
        self.fill_client_form(contact, mode)

        wd.find_element(By.NAME, "update").click()
        self.open_home_page()
        self.contact_cache = None

    def update_by_id(self, id, contact):
        wd = self.app.wd

        # updating mode
        mode = 1
        self.open_contact_by_id(id)
        self.fill_client_form(contact, mode)

        wd.find_element(By.NAME, "update").click()
        self.open_home_page()
        self.contact_cache = None

    def delete_first(self):
        self.delete_by_index(0)

    def press_delete_and_confirm(self, wd):
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        time.sleep(0.25)  # FIXME needs to find the way to avoid delaying

    def delete_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements(By.NAME, "selected[]")[index].click()
        self.press_delete_and_confirm(wd)
        self.open_home_page()
        self.contact_cache = None

    def delete_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element(By.CSS_SELECTOR, "input[value='" + id + "']").click()
        self.press_delete_and_confirm(wd)
        self.open_home_page()
        self.contact_cache = None

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
            wd.find_element(By.CSS_SELECTOR, "select[name='" + field_name + "'] > option[value='" + value + "']").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    def get_all(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()

            self.contact_cache = []
            elements = wd.find_elements(By.CSS_SELECTOR, "table tr[name='entry']")
            for element in elements:
                contact = element.find_elements(By.TAG_NAME, "td")
                id          = contact[0].find_element(By.NAME, "selected[]").get_attribute("value")
                firstname   = contact[2].text
                lastname    = contact[1].text
                address    = contact[3].text
                all_phones  = contact[5].text
                all_emails  = contact[4].text
                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname, address=address, all_phones=all_phones, all_emails=all_emails))

        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_by_index(index, "Edit")
        return Contact(
            id          = wd.find_element(By.NAME, "id").get_attribute("value"),
            firstname   = wd.find_element(By.NAME, "firstname").get_attribute("value"),
            lastname    = wd.find_element(By.NAME, "lastname").get_attribute("value"),
            home        = wd.find_element(By.NAME, "home").get_attribute("value"),
            mobile      = wd.find_element(By.NAME, "mobile").get_attribute("value"),
            work        = wd.find_element(By.NAME, "work").get_attribute("value"),
            phone2      = wd.find_element(By.NAME, "phone2").get_attribute("value"),
            email       = wd.find_element(By.NAME, "email").get_attribute("value"),
            email2      = wd.find_element(By.NAME, "email2").get_attribute("value"),
            email3      = wd.find_element(By.NAME, "email3").get_attribute("value")
        )

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_by_index(index, "Details")
        text = wd.find_element(By.ID, "content").text

        try: homephone = re.search("H: (.*)", text).group(1)
        except: homephone = ""

        try: workphone = re.search("W: (.*)", text).group(1)
        except: workphone = ""

        try: mobilephone = re.search("M: (.*)", text).group(1)
        except: mobilephone = ""

        try: secondaryphone = re.search("P: (.*)", text).group(1)
        except: secondaryphone = ""

        return Contact(home=homephone, mobile=mobilephone, work=workphone, phone2=secondaryphone)

    def add_contact_to_group(self, contact_id, group_id):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element(By.CSS_SELECTOR, "input[id='" + str(contact_id) + "'][name='selected[]']").click()
        self.fill_selector("to_group", str(group_id))
        wd.find_element(By.NAME, "add").click()
