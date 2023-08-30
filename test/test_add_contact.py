# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(
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
    app.session.logout()