from model.contact import Contact
from random import randrange
import re


def test_phones_on_home_page(app):
    test_info_on_home_page(app, 0, scope=("all_phones"))

def test_info_on_home_page(app, index=None, scope=None):
    contact_count = app.contact.count()
    if contact_count == 0:
        app.contact.create(Contact(firstname="FN TestForInfoDisplaying", lastname="LN TestForInfoDisplaying", address="Lalaland", mobile="(111) 111-11-111", email2="email2"))
        index = 0

    if index is None:
        index = randrange(contact_count)
        print("\nRandom Index: " + str(index))

    contact_from_home_page = app.contact.get_all()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)

    if scope is None or "firstname"  in scope: assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    if scope is None or "lastname"   in scope: assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    if scope is None or "address"    in scope: assert contact_from_home_page.address == contact_from_edit_page.address
    if scope is None or "all_phones" in scope: assert contact_from_home_page.all_phones == merge_phones(contact_from_edit_page)
    if scope is None or "all_emails" in scope: assert contact_from_home_page.all_emails == merge_emails(contact_from_edit_page)

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_info_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)

    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones(contact):
    return "\n".join(
        filter(lambda x: x != "",
               map(lambda x: clear(x),
                   filter(lambda x: x is not None, [contact.home, contact.mobile, contact.work, contact.phone2])
                   )
               )
    )

def merge_emails(contact):
    return "\n".join(
        filter(lambda x: x != "",
               map(lambda x: clear(x),
                   filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])
                   )
               )
    )
