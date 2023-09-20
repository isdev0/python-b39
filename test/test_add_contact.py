# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, json_contacts):
    old_contacts = app.contact.get_all()
    app.contact.create(json_contacts)

    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_all()

    old_contacts.append(json_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
