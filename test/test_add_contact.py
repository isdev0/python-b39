# -*- coding: utf-8 -*-
import random
import string
import pytest
import datetime
from model.contact import Contact


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits  + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_digits(maxlen):
    return "".join([random.choice(string.digits) for i in range(random.randrange(maxlen))])


def get_random_month_name():
    monthes = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
    index = random.randrange(11)
    return monthes[index]


testdata = [
    Contact(
        firstname   = random_string("FN", 10),
        middlename  = random_string("MN", 10),
        lastname    = random_string("LN", 10),
        nickname    = random_string("NN", 10),
        title       = random_string("Title", 10),
        company     = random_string("Company", 10),
        address     = random_string("Address1", 10),
        home        = random_digits(10),
        mobile      = random_digits(10),
        work        = random_digits(10),
        fax         = random_digits(10),
        email       = random_string("email1", 10),
        email2      = random_string("email2", 10),
        email3      = random_string("email3", 10),
        homepage    = random_string("hpage", 10),
        bday        = str(random.randrange(1, 31)),
        bmonth      = get_random_month_name(),
        byear       = str(random.randrange(1900, int(datetime.datetime.now().year))),
        aday        = str(random.randrange(1, 31)),
        amonth      = get_random_month_name(),
        ayear       = str(random.randrange(1990, int(datetime.datetime.now().year))),
        address2    = random_string("Address2", 10),
        phone2      = random_digits(10),
        notes       = random_string("notes", 10)
    )
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_all()
    app.contact.create(contact)

    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_all()

    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
