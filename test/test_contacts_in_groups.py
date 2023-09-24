# -*- coding: utf-8 -*-
import random
from model.contact import Contact
from model.group import Group


def test_add_random_contact_to_random_group(app, orm, suppress_asserts=False):
    if len(orm.get_all_groups()) == 0:
        app.group.create(Group(name="TestGroup"))

    groups = orm.get_all_groups()
    group = random.choice(groups)

    if len(orm.get_contacts_not_in_group(group)) == 0:
        app.contact.create(Contact(firstname="TestContactForGrouping"))

    contacts = orm.get_contacts_not_in_group(group)
    contact = random.choice(contacts)

    if not suppress_asserts: print("\nRandom Contact Id/Group Id: " + str(contact.id) + "/" + str(group.id))

    app.contact.add_contact_to_group(str(contact.id), str(group.id))
    if not suppress_asserts: assert(contact in orm.get_contacts_in_group(Group(id=str(group.id))))


def test_del_random_contact_from_not_empty_group(app, orm, suppress_asserts=False):
    if (len(orm.get_contact_ids_in_groups())) == 0:
        test_add_random_contact_to_random_group(app, orm, True)

    pairs = orm.get_contact_ids_in_groups()
    pair = random.choice(pairs)
    contact_id = pair[0]
    group_id = pair[1]

    print("\nRandom Contact Id/Group Id: " + str(contact_id) + "/" + str(group_id))

    app.contact.del_contact_from_group(str(contact_id), str(group_id))
    assert(orm.get_contact_by_id(contact_id)[0] in orm.get_contacts_not_in_group(Group(id=group_id)))
