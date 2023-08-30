# -*- coding: utf-8 -*-
from contact import Contact
from application import Application
import unittest


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_contact(self):
        self.app.login(username="admin", password="secret")
        self.app.create_contact(Contact(
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
        self.app.logout()

    def tearDown(self):
        self.app.destroy()

if __name__ == "__main__":
    unittest.main()
