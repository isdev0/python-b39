# -*- coding: utf-8 -*-
import random
from model.contact import Contact
from model.group import Group


def test_add_random_contact_to_random_group(app, orm):
    if len(orm.get_all_groups()) == 0:
        app.group.create(Group(name="TestGroup"))

    groups = orm.get_all_groups()
    group = random.choice(groups)

    print("\nRandom Group Id: " + str(group.id))
    print(group)

    contacts = orm.get_contacts_not_in_group(group)
    if len(contacts) == 0:
        contact = app.contact.create(Contact(firstname="TestContactForGrouping"))
    else:
        contact = random.choice(contacts)

    print("\nRandom Contact Id: " + str(contact.id))
    print(contact)

    app.contact.add_contact_to_group(contact.id, group.id)
    assert(contact in orm.get_contacts_in_group(Group(id=str(group.id))))
