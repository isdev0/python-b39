# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from contact import Contact
import unittest


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        #self.wd = webdriver.Chrome()
        self.wd.maximize_window()
        self.wd.implicitly_wait(30)

    def login(self, wd, username, password):
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").click()
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def create_contact(self, wd, contact):

        wd.find_element(By.LINK_TEXT, "add new").click()

        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)

        wd.find_element(By.NAME, "middlename").clear()
        wd.find_element(By.NAME, "middlename").send_keys(contact.middlename)

        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)

        wd.find_element(By.NAME, "nickname").clear()
        wd.find_element(By.NAME, "nickname").send_keys(contact.nickname)

        wd.find_element(By.NAME, "title").clear()
        wd.find_element(By.NAME, "title").send_keys(contact.title)

        wd.find_element(By.NAME, "company").clear()
        wd.find_element(By.NAME, "company").send_keys(contact.company)

        wd.find_element(By.NAME, "address").clear()
        wd.find_element(By.NAME, "address").send_keys(contact.address)

        wd.find_element(By.NAME, "home").click()
        wd.find_element(By.NAME, "home").clear()
        wd.find_element(By.NAME, "home").send_keys(contact.home)

        wd.find_element(By.NAME, "mobile").clear()
        wd.find_element(By.NAME, "mobile").send_keys(contact.mobile)

        wd.find_element(By.NAME, "work").clear()
        wd.find_element(By.NAME, "work").send_keys(contact.work)

        wd.find_element(By.NAME, "fax").clear()
        wd.find_element(By.NAME, "fax").send_keys(contact.fax)

        wd.find_element(By.NAME, "email").click()
        wd.find_element(By.NAME, "email").clear()
        wd.find_element(By.NAME, "email").send_keys(contact.email)

        wd.find_element(By.NAME, "email2").clear()
        wd.find_element(By.NAME, "email2").send_keys(contact.email2)

        wd.find_element(By.NAME, "email3").clear()
        wd.find_element(By.NAME, "email3").send_keys(contact.email3)

        wd.find_element(By.NAME, "homepage").click()
        wd.find_element(By.NAME, "homepage").clear()
        wd.find_element(By.NAME, "homepage").send_keys(contact.homepage)

        wd.find_element(By.NAME, "bday").click()
        Select(wd.find_element(By.NAME, "bday")).select_by_visible_text(contact.bday)
        wd.find_element(By.CSS_SELECTOR, "select[name=\"bday\"] > option[value=\""+contact.bday+"\"]").click()

        wd.find_element(By.NAME, "bmonth").click()
        Select(wd.find_element(By.NAME, "bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element(By.CSS_SELECTOR, "select[name=\"bmonth\"] > option[value=\""+contact.bmonth+"\"]").click()

        wd.find_element(By.NAME, "byear").click()
        wd.find_element(By.NAME, "byear").clear()
        wd.find_element(By.NAME, "byear").send_keys(contact.byear)

        wd.find_element(By.NAME, "aday").click()
        Select(wd.find_element(By.NAME, "aday")).select_by_visible_text(contact.aday)
        wd.find_element(By.CSS_SELECTOR, "select[name=\"aday\"] > option[value=\""+contact.aday+"\"]").click()

        wd.find_element(By.NAME, "amonth").click()
        Select(wd.find_element(By.NAME, "amonth")).select_by_visible_text(contact.amonth)
        wd.find_element(By.CSS_SELECTOR, "select[name=\"amonth\"] > option[value=\""+contact.amonth+"\"]").click()

        wd.find_element(By.NAME, "ayear").click()
        wd.find_element(By.NAME, "ayear").clear()
        wd.find_element(By.NAME, "ayear").send_keys(contact.ayear)

        wd.find_element(By.NAME, "theform").click()
        wd.find_element(By.NAME, "new_group").click()
        wd.find_element(By.NAME, "new_group").click()

        wd.find_element(By.NAME, "address2").click()
        wd.find_element(By.NAME, "address2").clear()
        wd.find_element(By.NAME, "address2").send_keys(contact.address2)

        wd.find_element(By.NAME, "phone2").click()
        wd.find_element(By.NAME, "phone2").clear()
        wd.find_element(By.NAME, "phone2").send_keys(contact.phone2)

        wd.find_element(By.NAME, "notes").clear()
        wd.find_element(By.NAME, "notes").send_keys(contact.notes)

        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()

    def open_internal_page(self, wd, tab):
        wd.find_element(By.LINK_TEXT, tab).click()

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True



    def test_add_contact(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        self.login(wd, username="admin", password="secret")
        self.create_contact(wd, Contact(
            firstname   = "Fname",
            middlename  = "Mname",
            lastname    = "Lname",
            nickname    = "Nname",
            title       = "Title",
            company     = "Company",
            address     = "Address1",
            home        = "111",
            mobile      = "222",
            work        = "333",
            fax         = "444",
            email       = "email1",
            email2      = "email2",
            email3      = "email3",
            homepage    = "hpage",
            bday        = "1",
            bmonth      = "January",
            byear       = "2001",
            aday        = "2",
            amonth      = "February",
            ayear       = "2002",
            address2    = "Address2",
            phone2      = "home",
            notes       = "notes"))
        self.open_internal_page(wd, "home")
        self.open_internal_page(wd, "Logout")

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
