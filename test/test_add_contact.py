# -*- coding: utf-8 -*-
import pytest

from model.contact import Contact


@pytest.mark.skip("needs json contacts only")
def test_add_simple_contact(app, data_contacts):
    app.contact.create(data_contacts)

#@pytest.mark.skip("needs just simple contacts atm")
def test_add_contact(app, orm, json_contacts):
    old_contacts = orm.get_all_contacts()
    app.contact.create(json_contacts)

    new_contacts = orm.get_all_contacts()
    assert len(old_contacts) + 1 == len(new_contacts)

    old_contacts.append(json_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
