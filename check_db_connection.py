from fixture.db import DbFixture
from fixture.orm import ORMFixture
from model.group import Group

#db = DbFixture(host="localhost", port=3306, database="addressbook", user="root", password="")
db = ORMFixture(host="localhost", port=3306, database="addressbook", user="root", password="")

try:
    groups = db.get_all_groups()
    print("\n")
    for group in groups:
        print(group)
    print(len(groups))

    contacts = db.get_all_contacts()
    print("\n")
    for contact in contacts:
        print(contact)
    print(len(contacts))

    l = db.get_group_by_id("199")
    print("\n")
    for item in l:
        print(item)
    print(len(l))

    l = db.get_contacts_in_group(Group(id="199"))
    print("\n")
    for item in l:
        print(item)
    print(len(l))

    l = db.get_contacts_not_in_group(Group(id="199"))
    print("\n")
    for item in l:
        print(item)
    print(len(l))

finally:
    pass#db.destroy()
