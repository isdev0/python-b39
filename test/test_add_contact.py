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
        notes       = "notes"
    )

    old_contacts = app.contact.getAll()

    app.contact.create(contact)

    new_contacts = app.contact.getAll()
    assert len(old_contacts) + 1 == len(new_contacts)

    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
