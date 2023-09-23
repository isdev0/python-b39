# -*- coding: utf-8 -*-
import random
from model.contact import Contact


def test_edit_random_contact(app, orm):
    if len(orm.get_all_contacts()) == 0:
        app.contact.create(Contact(firstname="TestForEditing"))

    old_contacts = orm.get_all_contacts()
    old_contact = random.choice(old_contacts)

    print("\nRandom Id: " + str(old_contact.id))
    new_contact = Contact(
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
        notes       = "notes9999"
    )
    new_contact.id = old_contact.id

    app.contact.update_by_id(old_contact.id, new_contact)

    new_contacts = orm.get_all_contacts()
    assert len(old_contacts) == len(new_contacts)

    old_contacts = list(map(lambda x: x if x != old_contact else new_contact, old_contacts))
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
