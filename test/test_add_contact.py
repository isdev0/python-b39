# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    contact = Contact(
        firstname   = "Fname",
        middlename  = "Mname",
        lastname    = "Lname",
        nickname    = "Nname",
        title       = "Title",
        company     = "Company",
        address     = "Address1",
        home        = "111-111",
        mobile      = "(222)222",
        work        = "333 333",
        fax         = "44-44-44",
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
        phone2      = "555555",
        notes       = "notes"
    )

    old_contacts = app.contact.get_all()

    app.contact.create(contact)

    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_all()

    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
