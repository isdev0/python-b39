# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_delete_random_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="TestForDeleting"))

    old_contacts = app.contact.get_all()
    index = randrange(len(old_contacts))
    print("\nRandom Index: " + str(index))
    app.contact.delete_by_index(index)

    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_all()

    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
