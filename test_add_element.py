# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class TestAddElement(unittest.TestCase):
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

    def test_add_element(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        self.login(wd, username="admin", password="secret")
        wd.find_element(By.LINK_TEXT, "add new").click()
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys("Fname")
        wd.find_element(By.NAME, "middlename").clear()
        wd.find_element(By.NAME, "middlename").send_keys("Mname")
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys("Lname")
        wd.find_element(By.NAME, "nickname").clear()
        wd.find_element(By.NAME, "nickname").send_keys("Nname")
        wd.find_element(By.NAME, "title").clear()
        wd.find_element(By.NAME, "title").send_keys("Title")
        wd.find_element(By.NAME, "company").clear()
        wd.find_element(By.NAME, "company").send_keys("Company")
        wd.find_element(By.NAME, "address").clear()
        wd.find_element(By.NAME, "address").send_keys("Address1")
        wd.find_element(By.NAME, "home").click()
        wd.find_element(By.NAME, "home").clear()
        wd.find_element(By.NAME, "home").send_keys("111")
        wd.find_element(By.NAME, "mobile").clear()
        wd.find_element(By.NAME, "mobile").send_keys("222")
        wd.find_element(By.NAME, "work").clear()
        wd.find_element(By.NAME, "work").send_keys("333")
        wd.find_element(By.NAME, "fax").clear()
        wd.find_element(By.NAME, "fax").send_keys("444")
        wd.find_element(By.NAME, "email").click()
        wd.find_element(By.NAME, "email").clear()
        wd.find_element(By.NAME, "email").send_keys("email1")
        wd.find_element(By.NAME, "email2").clear()
        wd.find_element(By.NAME, "email2").send_keys("email2")
        wd.find_element(By.NAME, "email3").clear()
        wd.find_element(By.NAME, "email3").send_keys("email3")
        wd.find_element(By.NAME, "homepage").click()
        wd.find_element(By.NAME, "homepage").clear()
        wd.find_element(By.NAME, "homepage").send_keys("hpage")
        wd.find_element(By.NAME, "bday").click()
        Select(wd.find_element(By.NAME, "bday")).select_by_visible_text("1")
        wd.find_element(By.XPATH, "//option[@value='1']").click()
        wd.find_element(By.NAME, "bmonth").click()
        Select(wd.find_element(By.NAME, "bmonth")).select_by_visible_text("January")
        wd.find_element(By.XPATH, "//option[@value='January']").click()
        wd.find_element(By.NAME, "byear").click()
        wd.find_element(By.NAME, "byear").clear()
        wd.find_element(By.NAME, "byear").send_keys("2001")
        wd.find_element(By.NAME, "aday").click()
        Select(wd.find_element(By.NAME, "aday")).select_by_visible_text("2")
        wd.find_element(By.XPATH, "//div[@id='content']/form/select[3]/option[4]").click()
        wd.find_element(By.NAME, "amonth").click()
        Select(wd.find_element(By.NAME, "amonth")).select_by_visible_text("February")
        wd.find_element(By.XPATH, "//div[@id='content']/form/select[4]/option[3]").click()
        wd.find_element(By.NAME, "ayear").click()
        wd.find_element(By.NAME, "ayear").clear()
        wd.find_element(By.NAME, "ayear").send_keys("2002")
        wd.find_element(By.NAME, "theform").click()
        wd.find_element(By.NAME, "new_group").click()
        wd.find_element(By.NAME, "new_group").click()
        wd.find_element(By.NAME, "address2").click()
        wd.find_element(By.NAME, "address2").clear()
        wd.find_element(By.NAME, "address2").send_keys("Address2")
        wd.find_element(By.NAME, "phone2").click()
        wd.find_element(By.NAME, "phone2").clear()
        wd.find_element(By.NAME, "phone2").send_keys("home")
        wd.find_element(By.NAME, "notes").clear()
        wd.find_element(By.NAME, "notes").send_keys("notes")
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
        wd.find_element(By.LINK_TEXT, "home").click()

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
