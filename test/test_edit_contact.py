# -*- coding: utf-8 -*-
from model.contact import Contact

def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.update_first(Contact(
        firstname   = "Fname9999",
        middlename  = "Mname9999",
        lastname    = "Lname9999",
        nickname    = "Nname9999",
        title       = "Title9999",
        company     = "Company9999",
        address     = "Address19999",
        home        = "1119999",
        mobile      = "2229999",
        work        = "3339999",
        fax         = "4449999",
        email       = "email19999",
        email2      = "email29999",
        email3      = "email39999",
        homepage    = "hpage9999",
        bday        = "2",
        bmonth      = "March",
        byear       = "2011",
        aday        = "3",
        amonth      = "May",
        ayear       = "2012",
        address2    = "Address29999",
        phone2      = "home9999",
        notes       = "notes9999"))
    app.session.logout()
