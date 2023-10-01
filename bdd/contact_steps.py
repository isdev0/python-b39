import random
from pytest_bdd import given, when, then, parsers
from model.contact import Contact


@given("a contact list", target_fixture="contact_list")
def contact_list(db):
    return db.get_all_contacts()


@given(parsers.parse("a contact with {firstname}, {lastname}, {address}, {mobile}, {email}, {email2} and {email3}"), target_fixture="new_contact")
def new_contact(firstname, lastname, address, mobile, email, email2, email3):
    return Contact(firstname=firstname, lastname=lastname, address=address, mobile=mobile, email=email, email2=email2, email3=email3)


@given("a non-empty contact list", target_fixture="non_empty_contact_list")
def non_empty_contact_list(app, db):
    if len(db.get_all_contacts()) == 0:
        app.contact.create(Contact(firstname="ContactForAction"))
    return db.get_all_contacts()


@given("a random contact in the list", target_fixture="random_contact")
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when("I add the contact to the list")
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)


@when("I delete the contact from the list")
def delete_contact(app, random_contact):
    app.contact.delete_by_id(random_contact.id)


@when("I update a contact in the list with the contact")
def update_contact(app, random_contact, new_contact):
    app.contact.update_by_id(random_contact.id, new_contact)


@then("the new contact list is equal to the old contact list with the added contact")
def verify_contact_added(db, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_all_contacts()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@then("the new contact list is equal to the old contact list with updated contact")
def verify_contact_updated(db, non_empty_contact_list, random_contact, new_contact):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_all_contacts()
    assert len(old_contacts) == len(new_contacts)

    old_contacts = list(map(lambda x: x if x != random_contact else new_contact, old_contacts))
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@then("the new contact list is equal to the old contact list without the deleted")
def verify_contact_deleted(db, non_empty_contact_list, random_contact):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_all_contacts()
    assert len(old_contacts) - 1 == len(new_contacts)

    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
