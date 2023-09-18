# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="TestForDeleting"))

    old_contacts = app.contact.getAll()

    app.contact.delete_first()

    new_contacts = app.contact.getAll()
    assert len(old_contacts) - 1 == len(new_contacts)

    old_contacts[0:0+1] = []
    assert old_contacts == new_contacts
