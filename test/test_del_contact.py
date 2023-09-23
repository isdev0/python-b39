# -*- coding: utf-8 -*-
import random
from model.contact import Contact


def test_delete_random_contact(app, orm):
    if len(orm.get_all_contacts()) == 0:
        app.contact.create(Contact(firstname="TestForDeleting"))

    old_contacts = orm.get_all_contacts()
    contact = random.choice(old_contacts)

    print("\nRandom Id: " + str(contact.id))
    app.contact.delete_by_id(contact.id)

    new_contacts = orm.get_all_contacts()
    assert len(old_contacts) - 1 == len(new_contacts)

    old_contacts.remove(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
