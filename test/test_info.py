# -*- coding: utf-8 -*-
from model.contact import Contact


def test_all_info_on_home_page(app, orm):
    if len(orm.get_all_contacts()) == 0:
        app.contact.create(Contact(firstname="FN TestForInfoDisplaying", lastname="LN TestForInfoDisplaying", address="Lalaland", mobile="(111) 111-11-111", email2="email2"))

    contacts_from_home_page = app.contact.get_all()
    contacts_from_database  = orm.get_all_contacts(autoaggregation=True)

    assert len(contacts_from_home_page) == len(contacts_from_database)
    assert sorted(contacts_from_home_page, key=Contact.id_or_max) == sorted(contacts_from_database, key=Contact.id_or_max)
